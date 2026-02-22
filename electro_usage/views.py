from django.shortcuts import render
import json

def menu(request):
    consumption_history = []
    final_consumption = None

    if request.method == "POST":
        apartments = int(request.POST.get("apartments", 0))
        infrastructure = int(request.POST.get("infrastructure", 0))
        buildings = int(request.POST.get("buildings", 0))

        apt_consumption = int(request.POST.get("apt_consumption", 0))
        house_consumption = int(request.POST.get("house_consumption", 0))
        public_consumption = int(request.POST.get("public_consumption", 0))

        E0 = (
            apartments * apt_consumption * 12 +
            buildings * house_consumption * 12 +
            infrastructure * public_consumption * 12
        )

        measures = {
            "LED": {"cost": 15, "effect": 0.08},
            "Insulation": {"cost": 25, "effect": 0.15},
            "Solar": {"cost": 30, "effect": 0.20},
            "Smart meters": {"cost": 10, "effect": 0.05},
            "Smart home": {"cost": 6, "effect": 0.03}
        }

        def greedy_strategy(budget):
            measures_list = list(measures.items())
            n = len(measures_list)
            for i in range(n):
                for j in range(0, n - i - 1):
                    eff1 = measures_list[j][1]["effect"] / measures_list[j][1]["cost"]
                    eff2 = measures_list[j + 1][1]["effect"] / measures_list[j + 1][1]["cost"]
                    if eff1 < eff2:
                        measures_list[j], measures_list[j + 1] = measures_list[j + 1], measures_list[j]
            sorted_measures = measures_list

            chosen = []
            remaining_budget = budget

            for name, data in sorted_measures:
                while remaining_budget >= data["cost"]:
                    chosen.append(name)
                    remaining_budget -= data["cost"]

            return chosen


        years = 10
        budget = 100
        current_consumption = E0

        consumption_history.append(current_consumption)

        for year in range(years):
            chosen_measures = greedy_strategy(budget)

            total_effect = 1
            for measure in chosen_measures:
                total_effect *= (1 - measures[measure]["effect"])

            new_consumption = current_consumption * total_effect
            savings = current_consumption - new_consumption

            budget = 100 + (savings / 1000000)
            current_consumption = new_consumption

            consumption_history.append(current_consumption)

        final_consumption = current_consumption


        context = {
            "consumption_history": json.dumps(consumption_history),
            "final_consumption": final_consumption,
        }

        return render(request, "result_calc.html", context)

    return render(request, "menu_calc.html")

