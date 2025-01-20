import NavBar from "../components/nav";
import Dashboard from "../components/dashboard";
import ChatDetails from "../components/details";

const Home = () => {
  return (
    <div class="chat-container">
      <NavBar />
      <Dashboard />
      <ChatDetails />
    </div>
  );
};

export default Home;
