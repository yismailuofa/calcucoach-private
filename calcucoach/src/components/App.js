import Header from "./Header";
import IntroText from "./IntroText";
import banner from "../assets/banner.jpg";

const appStyle = {
  backgroundColor: "#5AA9E6",
  display: "flex",
  height: "100vh",
  flexDirection: "column",
  alignItems: "center",
  color: "white",
  letterSpacing: "-0.06em",
};
export default function App() {
  return (
    <div style={appStyle}>
      <Header />
      <img
        src={banner}
        alt="A man tying his shoes in the gym."
        style={{
          width: "100vw",
          height: "100vh",
          objectFit: "cover",
          objectPosition: "40% 25%",
          opacity: "0.6",
        }}
      ></img>
      <IntroText />
      {/* button to start */}
    </div>
  );
}
