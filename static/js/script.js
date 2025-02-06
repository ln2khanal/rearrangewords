// Track correct drops
let correctDrops = 0;

// Placeholder for item data fetched from the server
let items = {};

// Fetch data from the server
function fetchItems() {
  fetch('/get_items')
    .then(response => {
      if (!response.ok) {
        throw new Error("Failed to fetch items data");
      }
      return response.json();
    })
    .then(data => {
      items = data; // Assign the fetched data to the items variable
      initializeData(); // Call a function to set up the game after fetching
    })
    .catch(error => {
      console.error("Error fetching items:", error);
      alert("Could not load items from the server.");
    });
}

// Function to initialize the game (generate columns and items)
function initializeData() {
  generateColumns();
  generateItems();
}

// Function to allow dropping
function allowDrop(event) {
  event.preventDefault(); // Allow dropping
}

// Function to handle dragging
function drag(event) {
  event.dataTransfer.setData("text", event.target.id); // Store the dragged element's id
}

function drop(event) {
  event.preventDefault();

  // Get the data (item id) of the dragged element
  const data = event.dataTransfer.getData("text");
  const draggedElement = document.getElementById(data);

  // Get the target where the item is being dropped
  const targetColumn = event.target;

  // Check if dropped in the taskRow
  if (targetColumn.id === "itemRow") {
    targetColumn.appendChild(draggedElement);
    correctDrops--; // Decrement correctDrops if dragged back
    updateProgress();
    return;
  }

  // Ensure we drop inside the column-body and not its header
  if (targetColumn.classList.contains("column-body")) {
    const targetColumnId = targetColumn.parentElement.id;

    // Get the category of the item being dragged
    const draggedTask = items.find(item => item.id === data);
    const targetCategory = targetColumnId;

    // Check if the dragged item's category matches the target column's category
    if (draggedTask.category === targetCategory) {
      // Append the dragged element to the column body
      targetColumn.appendChild(draggedElement);

      // Increment correct drop counter
      correctDrops++;

      // Update the progress bar
      updateProgress();
    } else {
      // If dropped in the wrong column, prevent dropping and give feedback, glow the screen
      const screen = document.getElementById("white-screen");
      screen.style.display = "block"; // Show white screen
      setTimeout(() => {
          screen.style.display = "none"; // Hide it after 4ms
      }, 300);
    }
  }
}

// Function to generate columns dynamically based on item categories
function generateColumns() {
  const container = document.getElementById("container");

  // Create a Set to get unique categories from the items
  const categories = new Set(Object.values(items).map(item => item.category));

  categories.forEach(category => {
    const column = document.createElement("div");
    column.id = category;
    column.classList.add("column");

    // Add a column title
    const columnTitle = document.createElement("h3");
    columnTitle.textContent = category.toUpperCase();
    column.appendChild(columnTitle);

    // Create a drop area inside the column-body
    const columnBody = document.createElement("div");
    columnBody.classList.add("column-body");
    columnBody.setAttribute("ondrop", "drop(event)");
    columnBody.setAttribute("ondragover", "allowDrop(event)");

    column.appendChild(columnBody);
    container.appendChild(column);
  });
}

// Function to generate items dynamically and place them in the item row
function generateItems() {
  const itemRow = document.getElementById("itemRow");

  Object.values(items).forEach(item => {
    const taskElement = document.createElement("div");
    taskElement.id = item.id;
    taskElement.classList.add("item");
    taskElement.setAttribute("draggable", "true");
    taskElement.setAttribute("ondragstart", "drag(event)");
    taskElement.textContent = item.content;

    itemRow.appendChild(taskElement);
  });
}

// Function to update the progress bar based on the number of correct drops
function updateProgress() {
  const totalTasks = Object.keys(items).length;
  const progressBar = document.getElementById("progressBar");
  const progressText = document.getElementById("progressText");

  const percentage = (correctDrops / totalTasks) * 100;

  // Update the progress bar width and text
  progressBar.style.width = `${percentage}%`;
  progressText.textContent = `${Math.round(percentage)}% Completed`;
}

// Fetch items and initialize the game
fetchItems();
