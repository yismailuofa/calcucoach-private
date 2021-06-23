import banner from "../assets/banner.jpg";
import IntroText from "./IntroText";

export default function Jumbotron() {
  return (
    <div
      style={{
        backgroundImage: `url(${banner})`,
        width: "100vw",
        height: "100%",
        backgroundSize: "cover",
        backgroundPosition: "40% 25%",
        opacity: "0.6",
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
    >
        <IntroText/>
    </div>
  );
}
