import "../styles/login.css";
import loginImage from "../assets/login.png";

const Login = () => {
  return (
    <div class="h-screen bg-black flex justify-center items-center font-muli">
      <div class="login-container flex justify-betweem items-center bg-white rounded-xl overflow-hidden ">
        <div class="image w-2/4">
          <img
            className="bg-cover bg-center bg-no-repeat w-full h-full "
            src={loginImage}
            alt=""
          />
        </div>
        <form class="login-form">
          <h1 className="text-xl text-center mb-6">Please Login Yourself!</h1>
          <div class="form-container">
            <div class="form-action">
              <label for="email">Email</label>
              <input type="email" required placeholder="Enter your email" />
            </div>
            <div class="form-action">
              <label for="password">Password</label>
              <input
                type="password"
                required
                placeholder="Enter your password"
              />
            </div>
          </div>
          <button type="submit" class="btn">
            Login
          </button>
          <p className="text-sm"> 
            Don't have an account? <a href="/register" className="font-bold">Register</a>
          </p>
        </form>
      </div>
    </div>
  );
};

export default Login;
