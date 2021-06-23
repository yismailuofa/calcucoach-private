import Faq from "./Faq";
import Title from "./Title";

export default function Header() {
  return (
    <div style={{width: "100%",display: "flex",alignItems: "center",justifyContent: "center", backgroundColor: "#5AA9E6"}}>
      <Title/>
      <Faq/>
    </div>
  );
}