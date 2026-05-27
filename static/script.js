let completed = 0;

function markDone(btn){

    // Prevent repeated clicks
    if(btn.disabled){
        return;
    }

    btn.disabled = true;

    btn.innerHTML = "Completed ✓";

    completed++;

    // Changed card → glass-card
    let total =
    document.querySelectorAll(".glass-card").length;

    let percentage =
    Math.round(
    (completed/total)*100
    );

    let bar =
    document.querySelector(".progress-bar");

    bar.style.width =
    percentage + "%";

    bar.innerHTML =
    percentage + "%";
} 