// ฟังก์ชันสำหรับการพับเมนู
function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("w-64");
    sidebar.classList.toggle("w-14");

    const textElements = document.querySelectorAll(".menu-text");
    textElements.forEach(element => {
        element.classList.toggle("hidden");
    });
}
