const apiUrl = "https://crudcrud.com/api/31c29820a60448a994e7d3afc1854beb/users";
const detailForm = document.getElementById("detailForm");
const detailStatus = document.getElementById("detailStatus");
const userTitle = document.getElementById("userTitle");
const deleteButton = document.getElementById("deleteButton");
const firstNameInput = document.getElementById("firstName");
const lastNameInput = document.getElementById("lastName");
const emailInput = document.getElementById("email");
const ageInput = document.getElementById("age");
const addressInput = document.getElementById("address");

function getQueryParam(name) {
  return new URLSearchParams(window.location.search).get(name);
}

async function fetchUserDetails(userId) {
  if (!userId) {
    renderError("Missing user ID in URL.");
    return;
  }

  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`);
    }

    const users = await response.json();
    const user = Array.isArray(users) ? users.find((item) => item._id === userId) : null;

    if (!user) {
      renderError("User not found.");
      return;
    }

    populateForm(user);
  } catch (error) {
    renderError("Unable to load user details. Please try again later.");
    console.error("Error fetching user details:", error);
  }
}

function populateForm(user) {
  userTitle.textContent = `${user.first_name || "Unknown"} ${user.last_name || ""}`.trim();
  firstNameInput.value = user.first_name || "";
  lastNameInput.value = user.last_name || "";
  emailInput.value = user.email || "";
  ageInput.value = user.age ?? "";
  addressInput.value = user.address || "";
}

function renderError(message) {
  detailStatus.textContent = message;
  detailStatus.style.color = "#f97316";
}

async function updateUser(userId, data) {
  const response = await fetch(`${apiUrl}/${encodeURIComponent(userId)}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return response;
}

async function deleteUser(userId) {
  const response = await fetch(`${apiUrl}/${encodeURIComponent(userId)}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return response;
}

const userId = getQueryParam("id");

detailForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  detailStatus.textContent = "Saving changes...";
  detailStatus.style.color = "var(--muted)";

  const body = {
    first_name: firstNameInput.value.trim(),
    last_name: lastNameInput.value.trim(),
    email: emailInput.value.trim(),
    age: Number(ageInput.value) || 0,
    address: addressInput.value.trim(),
  };

  try {
    await updateUser(userId, body);
    detailStatus.textContent = "User updated successfully.";
    detailStatus.style.color = "#22c55e";
    userTitle.textContent = `${body.first_name || "Unknown"} ${body.last_name || ""}`.trim();
  } catch (error) {
    detailStatus.textContent = "Unable to save changes. Please try again.";
    detailStatus.style.color = "#f97316";
    console.error("Error updating user:", error);
  }
});

deleteButton.addEventListener("click", async () => {
  const confirmed = window.confirm("Delete this user? This cannot be undone.");
  if (!confirmed) {
    return;
  }

  detailStatus.textContent = "Deleting user...";
  detailStatus.style.color = "var(--muted)";

  try {
    await deleteUser(userId);
    window.location.href = "index.html";
  } catch (error) {
    detailStatus.textContent = "Unable to delete user. Please try again.";
    detailStatus.style.color = "#f97316";
    console.error("Error deleting user:", error);
  }
});

fetchUserDetails(userId);
