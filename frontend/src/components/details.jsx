import "../styles/details.css";

const ChatDetails = () => {
  return (
    <div class="detail-container">
      <div class="heading flex justify-between items-center">
        <h1 className="font-bold text-xl">Chat Details</h1>
        <div class="icon text-lg text-black">
          <i class="fas fa-xmark"></i>
        </div>
      </div>

      <div class="detail my-5">
        <div class="detail-col">
          <h1>Photo & Videos</h1>
          <div class="content">
            <img
              src="https://randomuser.me/api/portraits/women/28.jpg"
              alt=""
            />
          </div>
        </div>
        <div class="detail-col">
          <h1>Photo & Videos</h1>
          <div class="content">
            <img
              src="https://randomuser.me/api/portraits/women/19.jpg"
              alt=""
            />
          </div>
        </div>
        <div class="detail-col">
          <h1>Photo & Videos</h1>
          <div class="content">
            <img
              src="https://randomuser.me/api/portraits/women/18.jpg"
              alt=""
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatDetails;
