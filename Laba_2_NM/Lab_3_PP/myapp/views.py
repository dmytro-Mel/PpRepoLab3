from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from .models import User, Wallet, Chain


# Aggregated report showing each user’s total balance across all wallets
def aggregate_report(request):
    report = []
    users = User.objects.all()
    for user in users:
        wallets = Wallet.objects.filter(user=user)
        total_balance = Chain.objects.filter(wallet__in=wallets).aggregate(Sum('balance'))['balance__sum'] or 0
        report.append({
            'username': user.username,
            'total_balance': total_balance
        })
    return JsonResponse({'report': report})


# Create a new User and redirect to wallet creation
@require_http_methods(["GET", "POST"])
def create_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        verif = request.POST.get('verif')

        if not username or not email or not password:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        # Create the user
        user = User.objects.create(
            username=username,
            email=email,
            password=password,
            verif=verif,
            create_date=timezone.now()
        )

        # Redirect to create_wallet with user ID
        return redirect('create_wallet', user_id=user.id)

    return render(request, 'create_user.html')


# Create a Wallet for a specific User
@require_http_methods(["GET", "POST"])
def create_wallet(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        Wallet.objects.create(user=user, create_date=timezone.now())
        return JsonResponse({'message': f'Wallet created for user {user.username}'})

    return render(request, 'create_wallet.html', {'user': user})


# Read User details
def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email})


# Update User details
@require_http_methods(["POST"])
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.username = request.POST.get('username', user.username)
    user.email = request.POST.get('email', user.email)
    user.password = request.POST.get('password', user.password)
    user.verif = request.POST.get('verif', user.verif)
    user.save()
    return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email})


# Delete User
@require_http_methods(["DELETE"])
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return JsonResponse({'message': f'User {user_id} deleted successfully.'})
