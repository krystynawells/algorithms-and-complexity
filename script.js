const projects = [
  {
    id: "week1",
    title: "Week 1 - Interactive CV",
    image: "https://raw.githubusercontent.com/krystynawells/profile-assets/main/monkey1.jpg",
  },
  {
    id: "week2",
    title: "Week 2 - Sorting Visualizer",
    image: "https://raw.githubusercontent.com/krystynawells/profile-assets/main/monkey6.jpg",
  },
  {
    id: "week3",
    title: "Week 3 - Binary Search",
    image: "https://raw.githubusercontent.com/krystynawells/profile-assets/main/monkey5.jpg",
  },
  {
    id: "week4",
    title: "Week 4 - Interactive Essay",
    image: "https://raw.githubusercontent.com/krystynawells/profile-assets/main/monkey4.jpg",
  },
  {
    id: "week5",
    title: "Week 5 - Tree Visualizer",
    image: "https://raw.githubusercontent.com/krystynawells/profile-assets/main/monkey3..jpg",
  },
  {
    id: "week6",
    title: "Week 6 - Genetic Algorithm",
    image: "https://raw.githubusercontent.com/krystynawells/profile-assets/main/a6076e16eb6c3911a1c5aa2698f4b940.jpg",
  },
  {
    id: "week7",
    title: "Week 7 - Graph Traversal",
    image: "https://raw.githubusercontent.com/krystynawells/profile-assets/main/9ebd00819d6de0e602a6b66008dfd900.jpg",
  },
    {
    id: "final_project",
    title: "Final Project - Fashion Algorithm",
    image: "https://raw.githubusercontent.com/krystynawells/profile-assets/main/48ab117e4a43b71cd6f9a0a1e9ac3738.jpg",
  },
];


const container = document.getElementById("project-container");

projects.forEach((proj) => {
  const card = document.createElement("div");
  card.className = "project-card";
  card.innerHTML = `
    <img src="${proj.image}" alt="${proj.title}">
    <div class="project-info">
      <h2>${proj.title}</h2>
    </div>
  `;
  card.addEventListener("click", () => {
    window.location.href = `projects/${proj.id}/docs/index.html`;
  });
  container.appendChild(card);
});
