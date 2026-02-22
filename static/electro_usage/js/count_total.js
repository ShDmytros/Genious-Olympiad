document.addEventListener("DOMContentLoaded", function () {

    const apartments = document.getElementById("apartments");
    const infrastructure = document.getElementById("infrastructure");
    const buildings = document.getElementById("buildings");
    const total = document.getElementById("total");

    function calculateTotal() {
        const sum =
            (parseInt(apartments.value) || 0) +
            (parseInt(infrastructure.value) || 0) +
            (parseInt(buildings.value) || 0);

        total.textContent = sum;
    }

    apartments.addEventListener("input", calculateTotal);
    infrastructure.addEventListener("input", calculateTotal);
    buildings.addEventListener("input", calculateTotal);
});