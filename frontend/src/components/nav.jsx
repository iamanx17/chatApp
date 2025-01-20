import "../styles/nav.css";

const NavBar = () => {
  return (
    <div class="nav-options">
      <h2>
        <a href="/">chatApp</a>
      </h2>
      <ul>
        <li>
          <i class="fas fa-message"></i>
          <span>All chats</span>
        </li>
        <li>
          <i class="fas fa-bolt"></i>
          <span>AI</span>
        </li>
        <li>
          <i class="fas fa-heart"></i>
          <span>Favourites</span>
        </li>
        <li>
          <i class="fas fa-user"></i>
          <span>Profile</span>
        </li>
        <li>
          <i class="fas fa-pen-to-square"></i>
          <span>Edit</span>
        </li>
      </ul>
      <div class="logout">
        <i class="fas fa-right-from-bracket"></i>
        <span>Logout</span>
      </div>
    </div>
  );
};

export default NavBar;
