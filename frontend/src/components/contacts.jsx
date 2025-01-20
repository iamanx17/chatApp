import "../styles/contacts.css";

const Contacts = () => {
  return (
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
            <img src="https://randomuser.me/api/portraits/men/75.jpg" alt="" />
          </div>
          <div class="profile-info">
            <h2 class="profile-title">John Doe</h2>
            <p class="profile-desc">Lorem, ipsum dolor.</p>
          </div>
          <span class="total">5</span>
        </div>

        <div class="profile">
          <div class="profile-image">
            <img src="https://randomuser.me/api/portraits/men/75.jpg" alt="" />
          </div>
          <div class="profile-info">
            <h2 class="profile-title">John Doe</h2>
            <p class="profile-desc">Lorem, ipsum dolor.</p>
          </div>
          <span class="total">5</span>
        </div>

        <div class="profile">
          <div class="profile-image">
            <img src="https://randomuser.me/api/portraits/men/75.jpg" alt="" />
          </div>
          <div class="profile-info">
            <h2 class="profile-title">John Doe</h2>
            <p class="profile-desc">Lorem, ipsum dolor.</p>
          </div>
          <span class="total">5</span>
        </div>
      </div>
    </div>
  );
};

export default Contacts;
