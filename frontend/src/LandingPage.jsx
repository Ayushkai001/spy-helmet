import { useNavigate } from "react-router-dom";

function LandingPage() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-br from-black via-gray-900 to-gray-800 text-white flex flex-col items-center justify-center p-6 space-y-6">
      <h1 className="text-5xl md:text-6xl font-bold text-center text-cyan-400 animate-pulse drop-shadow-lg underline decoration-cyan-400 decoration-4">
        SPY-HELMET SYSTEM : It see's what you can't
      </h1>
      <p className="text-center max-w-xl text-gray-300 text-lg md:text-xl">
        Revolutionizing safety with AI-powered fatigue monitoring. Track real-time mental and physical states with precision and style.
      </p>

      <div className="flex space-x-6">
        <button
          onClick={() => navigate("/login")}
          className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-xl shadow-lg transition transform hover:scale-105"
        >
          Login
        </button>
        <button
          onClick={() => navigate("/register")}
          className="bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-6 rounded-xl shadow-lg transition transform hover:scale-105"
        >
          Register
        </button>
      </div>
    </div>
  );
}

export default LandingPage;
