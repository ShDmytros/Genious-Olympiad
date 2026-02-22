// let measureCount = 0;

// function addMeasure() {
//     const submitButton = document.getElementById("submit");
//     submitButton.disabled = false;
//     measureCount++;

//     const container = document.getElementById("measuresContainer");

//     const div = document.createElement("div");

//     div.classList.add("flex", "flex-col", "gap-3", "p-4", "bg-gray-100", "rounded-2xl");

//     div.innerHTML = `
//         <label>Measure Name</label>
//         <input type="text" name="custom_name_${measureCount}"
//                class="rounded-xl p-2 shadow" required>

//         <label>Cost per unit</label>
//         <input type="number" name="custom_cost_${measureCount}"
//                class="rounded-xl p-2 shadow" required>

//         <label>Effect per unit</label>
//         <input type="number" step="0.01"
//                name="custom_effect_${measureCount}"
//                class="rounded-xl p-2 shadow" required>
//     `;

//     container.appendChild(div);
// }