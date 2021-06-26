import FaqButton from "./FaqButton";
import Title from "./Title";

export default function Header(props) {
  return (
    <div
      style={{
        width: "100vw",
        height: "8vw",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        boxShadow: "0vw 2px 20px black",
        position: "relative",
      }}
    >
      <Title />
      <FaqButton faqStep={props.faqStep}/>
    </div>
  );
}
