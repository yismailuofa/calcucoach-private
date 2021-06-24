import banner from "../assets/banner.jpg";
import IntroText from "./IntroText";

export default function Jumbotron() {
  return (
    <div
      style={{
        backgroundImage: `url(${banner})`,
        width: "100vw",
        height: "100vh",
        backgroundSize: "cover",
        backgroundPosition: "40% 25%",
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
    >
        <IntroText/>
    </div>
  );
}
