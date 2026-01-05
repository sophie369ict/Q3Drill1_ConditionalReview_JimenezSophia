from pyscript import document

def compute_average(event):
    # Get the input values
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)

    # Compute the average
    average = (score1 + score2) / 2

    # Determine pass/fail
    if average >= 75:
        result = "PASSED 🥹"
    else:
        result = "FAILED 😭"

    # Show results in the page
    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result