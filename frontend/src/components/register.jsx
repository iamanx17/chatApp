import "../styles/register.css";
import registerImage from "../assets/login.png";

const Register = () => {
  return (
    <div class="h-screen bg-black flex justify-center items-center font-muli">
      <div class="register-container flex justify-betweem items-center bg-white rounded-xl overflow-hidden">
        <div class="image w-2/4">
          <img
            className="bg-cover bg-center bg-no-repeat w-full h-full "
            src={registerImage}
            alt=""
          />
        </div>
        <form class="register-form">
          <h1 className="text-xl text-center mb-6">
            Please Register Yourself!
          </h1>
          <div class="form-container">
            <div class="form-row">
              <div class="form-col">
                <label for="first_name">First Name</label>
                <input
                  type="text"
                  required
                  placeholder="Enter your first name"
                />
              </div>
              <div class="form-col">
                <label for="last_name">Last Name</label>
                <input
                  type="text"
                  required
                  placeholder="Enter your last name"
                />
              </div>
            </div>

            <div class="form-col">
              <label for="email">Email</label>
              <input type="email" required placeholder="Enter your email" />
            </div>
            <div class="form-row">
              <div class="form-col">
                <label for="password1">Password</label>
                <input
                  type="password"
                  required
                  placeholder="Enter your password"
                />
              </div>
              <div class="form-col">
                <label for="password2">Confirm Password</label>
                <input
                  type="password"
                  required
                  placeholder="Enter your password"
                />
              </div>
            </div>
          </div>
          <button type="submit" class="btn">
            Register
          </button>
          <p className="text-sm">
            Already have an account?{" "}
            <a href="/login" className="font-bold">
              Login
            </a>
          </p>
        </form>
      </div>
    </div>
  );
};

export default Register;
