const apiUrl = "https://crudcrud.com/api/31c29820a60448a994e7d3afc1854beb/users";
const form = document.getElementById("createForm");
const formStatus = document.getElementById("formStatus");

async function createUser(data) {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error("Error creating user:", error);
    throw error;
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  formStatus.textContent = "Saving user...";
  formStatus.style.color = "var(--muted)";

  const formData = new FormData(form);
  const body = {
    first_name: formData.get("first_name")?.toString().trim() || "",
    last_name: formData.get("last_name")?.toString().trim() || "",
    email: formData.get("email")?.toString().trim() || "",
    age: Number(formData.get("age")) || 0,
    address: formData.get("address")?.toString().trim() || "",
  };

  try {
    await createUser(body);
    formStatus.textContent = "User created successfully. Redirecting...";
    formStatus.style.color = "#22c55e";
    form.reset();
    window.setTimeout(() => {
      window.location.href = "index.html";
    }, 700);
  } catch (error) {
    formStatus.textContent = "Could not create user. Please try again.";
    formStatus.style.color = "#f97316";
  }
});
