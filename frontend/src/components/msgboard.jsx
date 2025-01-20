import '../styles/msgBoard.css'

const MsgBoard = () => {
  return (
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
            <i class="fas fa-info"></i>
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
  );
};


export default MsgBoard