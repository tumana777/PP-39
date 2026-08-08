const apiUrl = "https://crudcrud.com/api/31c29820a60448a994e7d3afc1854beb/users";
const statusEl = document.getElementById("status");
const userListEl = document.getElementById("userList");
const paginationEl = document.getElementById("pagination");
const searchInput = document.getElementById("searchInput");

const pageSize = 5;
let users = [];
let filteredUsers = [];
let currentPage = 1;

async function fetchUsers() {
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`);
    }

    users = sortUsers(await response.json());
    filteredUsers = users;

    if (!Array.isArray(users) || users.length === 0) {
      statusEl.textContent = "No users found.";
      paginationEl.innerHTML = "";
      return;
    }

    renderPage(1);
  } catch (error) {
    statusEl.textContent = "Unable to load users. Please try again later.";
    paginationEl.innerHTML = "";
    console.error("Error fetching users:", error);
  }
}

function sortUsers(userList) {
  return Array.isArray(userList)
    ? [...userList].sort((a, b) => {
        const nameA = `${a.first_name || ""} ${a.last_name || ""}`.trim().toLowerCase();
        const nameB = `${b.first_name || ""} ${b.last_name || ""}`.trim().toLowerCase();
        return nameA.localeCompare(nameB, undefined, { sensitivity: "base" });
      })
    : [];
}

function applySearchFilter(query) {
  if (!query) {
    filteredUsers = users;
    return;
  }

  const normalized = query.trim().toLowerCase();
  filteredUsers = users.filter((user) => {
    const fullName = `${user.first_name || ""} ${user.last_name || ""}`.trim().toLowerCase();
    const email = (user.email || "").toLowerCase();
    const address = (user.address || "").toLowerCase();
    return fullName.includes(normalized) || email.includes(normalized) || address.includes(normalized);
  });
}

function renderPage(page) {
  const totalPages = Math.max(1, Math.ceil(filteredUsers.length / pageSize));
  currentPage = Math.min(Math.max(page, 1), totalPages);

  const start = (currentPage - 1) * pageSize;
  const pageUsers = filteredUsers.slice(start, start + pageSize);

  if (filteredUsers.length === 0) {
    statusEl.textContent = "No users match the current search.";
    userListEl.innerHTML = "";
    paginationEl.innerHTML = "";
    return;
  }

  statusEl.textContent = `Showing ${pageUsers.length} of ${filteredUsers.length} user${filteredUsers.length === 1 ? "" : "s"} — page ${currentPage} of ${totalPages}.`;
  renderUsers(pageUsers);
  renderPagination(totalPages);
}

function renderUsers(usersToShow) {
  userListEl.innerHTML = "";

  usersToShow.forEach((user) => {
    const card = document.createElement("article");
    card.className = "user-card";

    const heading = document.createElement("div");
    heading.className = "card-header";

    const linkEl = document.createElement("a");
    linkEl.className = "card-link";
    linkEl.href = `detail.html?id=${encodeURIComponent(user._id || "")}`;
    linkEl.textContent = `${user.first_name || "Unknown"} ${user.last_name || ""}`.trim();

    heading.appendChild(linkEl);
    card.appendChild(heading);
    userListEl.appendChild(card);
  });
}

function renderPagination(totalPages) {
  paginationEl.innerHTML = "";

  if (totalPages <= 1) {
    return;
  }

  const prevButton = createPageButton("Previous", () => renderPage(currentPage - 1));
  prevButton.disabled = currentPage === 1;
  paginationEl.appendChild(prevButton);

  for (let page = 1; page <= totalPages; page += 1) {
    const pageButton = createPageButton(String(page), () => renderPage(page));
    if (page === currentPage) {
      pageButton.classList.add("active");
      pageButton.disabled = true;
    }
    paginationEl.appendChild(pageButton);
  }

  const nextButton = createPageButton("Next", () => renderPage(currentPage + 1));
  nextButton.disabled = currentPage === totalPages;
  paginationEl.appendChild(nextButton);
}

function createPageButton(label, onClick) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "pagination-button";
  button.textContent = label;
  button.addEventListener("click", onClick);
  return button;
}

searchInput.addEventListener("input", (event) => {
  applySearchFilter(event.target.value);
  renderPage(1);
});

fetchUsers();
