#!/usr/bin/env python3
"""
BBQ Rub Sodium Calculator

This calculator helps determine how much additional kosher salt to add to pork ribs
when using commercial BBQ rubs that already contain sodium.
"""

def calculate_additional_salt(weight_lbs, rub_sodium_per_quarter_tsp, rub_amount_tsp, target_salt_per_lb_mg=1000):
    """
    Calculate additional kosher salt needed for BBQ ribs.
    
    Args:
        weight_lbs (float): Weight of ribs in pounds
        rub_sodium_per_quarter_tsp (int): Sodium content in mg per 1/4 tsp of rub
        rub_amount_tsp (float): Amount of rub to use in teaspoons
        target_salt_per_lb_mg (int): Target sodium per pound (default: 1000mg, about 1/2 tsp kosher salt)
    
    Returns:
        dict: Results including sodium from rub, target sodium, and additional salt needed
    """
    
    # Calculate total target sodium for the meat
    total_target_sodium_mg = weight_lbs * target_salt_per_lb_mg
    
    # Calculate sodium from the BBQ rub
    # Convert rub amount to quarter-teaspoons for calculation
    quarter_tsp_of_rub = rub_amount_tsp * 4
    sodium_from_rub_mg = quarter_tsp_of_rub * rub_sodium_per_quarter_tsp
    
    # Calculate additional sodium needed
    additional_sodium_needed_mg = max(0, total_target_sodium_mg - sodium_from_rub_mg)
    
    # Convert to kosher salt (approximately 480mg sodium per 1/4 tsp kosher salt)
    kosher_salt_sodium_per_quarter_tsp = 480
    additional_kosher_salt_quarter_tsp = additional_sodium_needed_mg / kosher_salt_sodium_per_quarter_tsp
    additional_kosher_salt_tsp = additional_kosher_salt_quarter_tsp / 4
    
    return {
        'weight_lbs': weight_lbs,
        'target_total_sodium_mg': total_target_sodium_mg,
        'rub_amount_tsp': rub_amount_tsp,
        'sodium_from_rub_mg': sodium_from_rub_mg,
        'additional_sodium_needed_mg': additional_sodium_needed_mg,
        'additional_kosher_salt_tsp': round(additional_kosher_salt_tsp, 2),
        'additional_kosher_salt_quarter_tsp': round(additional_kosher_salt_quarter_tsp, 2)
    }

def print_results(results):
    """Print formatted results."""
    print(f"\n=== BBQ Salt Calculator Results ===")
    print(f"Rib weight: {results['weight_lbs']} lbs")
    print(f"BBQ rub amount: {results['rub_amount_tsp']} tsp")
    print(f"Target total sodium: {results['target_total_sodium_mg']} mg")
    print(f"Sodium from BBQ rub: {results['sodium_from_rub_mg']} mg")
    print(f"Additional sodium needed: {results['additional_sodium_needed_mg']} mg")
    print(f"\n--- Additional Kosher Salt Needed ---")
    print(f"Teaspoons: {results['additional_kosher_salt_tsp']} tsp")
    print(f"Quarter-teaspoons: {results['additional_kosher_salt_quarter_tsp']} (1/4 tsp)")
    
    if results['additional_kosher_salt_tsp'] == 0:
        print("\n✅ No additional salt needed! Your rub has enough sodium.")
    elif results['additional_kosher_salt_tsp'] < 0.25:
        print(f"\n💡 Just a pinch of kosher salt needed!")
    else:
        print(f"\n🧂 Add {results['additional_kosher_salt_tsp']} tsp of kosher salt")

def main():
    """Main calculator interface."""
    print("🍖 BBQ Rub Sodium Calculator 🍖")
    print("Help determine additional kosher salt needed for your ribs!")
    
    # Example calculations for your specific question
    print("\n" + "="*50)
    print("EXAMPLE: 5 lbs of ribs with different rubs")
    print("="*50)
    
    # Scenario 1: Low sodium rub (110mg per 1/4 tsp)
    print("\n--- Scenario 1: Low Sodium Rub (110mg/1/4 tsp) ---")
    # Assuming 2 tbsp (6 tsp) of rub for 5 lbs of ribs
    results1 = calculate_additional_salt(
        weight_lbs=5,
        rub_sodium_per_quarter_tsp=110,
        rub_amount_tsp=6,  # 2 tablespoons
        target_salt_per_lb_mg=1000  # Recommended: ~1/2 tsp kosher salt per lb
    )
    print_results(results1)
    
    # Scenario 2: High sodium rub (200mg per 1/4 tsp)
    print("\n--- Scenario 2: High Sodium Rub (200mg/1/4 tsp) ---")
    results2 = calculate_additional_salt(
        weight_lbs=5,
        rub_sodium_per_quarter_tsp=200,
        rub_amount_tsp=6,  # 2 tablespoons
        target_salt_per_lb_mg=1000
    )
    print_results(results2)
    
    # Interactive calculator
    print("\n" + "="*50)
    print("CUSTOM CALCULATOR")
    print("="*50)
    
    try:
        weight = float(input("\nEnter weight of ribs (lbs): "))
        rub_sodium = int(input("Enter sodium per 1/4 tsp of rub (mg): "))
        rub_amount = float(input("Enter amount of rub to use (tsp): "))
        
        # Optional: custom target
        use_default = input("\nUse default target (1000mg sodium per lb)? (y/n): ").lower()
        if use_default == 'n':
            target = int(input("Enter target sodium per lb (mg): "))
        else:
            target = 1000
        
        results = calculate_additional_salt(weight, rub_sodium, rub_amount, target)
        print_results(results)
        
        # Additional tips
        print("\n" + "="*30)
        print("💡 TIPS:")
        print("="*30)
        print("• Kosher salt: ~480mg sodium per 1/4 tsp")
        print("• Table salt: ~580mg sodium per 1/4 tsp")
        print("• General rule: 1/2 tsp kosher salt per lb of meat")
        print("• Apply salt 40+ minutes before cooking for best results")
        print("• Consider the saltiness of your BBQ sauce too!")
        
    except ValueError:
        print("Please enter valid numbers!")
    except KeyboardInterrupt:
        print("\n\nThanks for using the BBQ calculator! 🍖")

if __name__ == "__main__":
    main()
