import Faq from "./Faq";
import Title from "./Title";

export default function Header() {
  return (
    <div
      style={{
        width: "100vw",
        height: "8vw",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        boxShadow: "0vw 20px 40px black",
        position: "relative",
      }}
    >
      <Title />
      <Faq />
    </div>
  );
}
