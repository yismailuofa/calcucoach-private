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
        backgroundPosition: "45% 55%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center"
      }}
    >
        <IntroText/>
    </div>
  );
}
