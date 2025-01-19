import "../styles/home.css";

const Home = () => {
  return (
    <div class="chat-container">
      <div class="nav-options">
        <h2>chatApp</h2>
        <ul>
          <li>
            <i class="fas fa-message"></i> <span>All chats</span>
          </li>
          <li>
            <i class="fas fa-bolt"></i> <span>AI</span>
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
      <div class="main">
        <div class="chat">
          <div class="search">
            <div class="search-icon">
              <i class="fas fa-magnifying-glass"></i>
            </div>
            <input type="text" id="" placeholder="search" />
          </div>
          <div class="profiles">
            <div class="profile">
              <div class="profile-image">
                <img
                  src="https://randomuser.me/api/portraits/men/75.jpg"
                  alt=""
                />
              </div>
              <div class="profile-info">
                <h2 class="profile-title">John Doe</h2>
                <p class="profile-desc">Lorem, ipsum dolor.</p>
              </div>
              <span class="total">5</span>
            </div>

            <div class="profile">
              <div class="profile-image">
                <img
                  src="https://randomuser.me/api/portraits/men/75.jpg"
                  alt=""
                />
              </div>
              <div class="profile-info">
                <h2 class="profile-title">John Doe</h2>
                <p class="profile-desc">Lorem, ipsum dolor.</p>
              </div>
              <span class="total">5</span>
            </div>

            <div class="profile">
              <div class="profile-image">
                <img
                  src="https://randomuser.me/api/portraits/men/75.jpg"
                  alt=""
                />
              </div>
              <div class="profile-info">
                <h2 class="profile-title">John Doe</h2>
                <p class="profile-desc">Lorem, ipsum dolor.</p>
              </div>
              <span class="total">5</span>
            </div>
          </div>
        </div>
        <div class="message-body">
          <div class="upper">
            <div class="heading">
              <h1 class="upper-title">chatApp</h1>
              <p>Lorem ipsum dolor sit amet.</p>
            </div>
            <div class="upper-icons">
              <div class="icon">
                <i class="fas fa-magnifying-glass"></i>
              </div>
              <div class="icon">
                <i class="fas fa-phone"></i>
              </div>
              <div class="icon">
                <i class="fas fa-bars"></i>
              </div>
            </div>
          </div>
          <div class="message">
            <div class="user">
              <div class="user-image">
                <img
                  src="https://randomuser.me/api/portraits/women/12.jpg"
                  alt=""
                />
              </div>
              <div class="user-message">
                <p>Hey there, how are you</p>
              </div>
            </div>

            <div class="user">
              <div class="user-image">
                <img
                  src="https://randomuser.me/api/portraits/women/12.jpg"
                  alt=""
                />
              </div>
              <div class="user-message">
                <p>Hey there, how are you</p>
              </div>
            </div>
          </div>
          <div class="message-input">
            <i class="fas fa-paperclip"></i>
            <input type="text" placeholder="Enter your message" />
            <i class="fa-regular fa-paper-plane"></i>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
