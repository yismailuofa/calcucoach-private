export default function FaqButton(props) {
  return (
      <button
      style={{
        fontSize: "3.5vw",
        letterSpacing: "-0.06em",
        textDecoration: "none",
        color: "white",
        fontFamily: "Poppins",
        display: "flex",
        alignItems: "center",
        height: "100%",
        backgroundColor: "#4a86ba",
        border: "none",
        cursor: "pointer",
        padding: "0"
      }}
      onClick={props.faqStep}
    >
      faq
    </button>    
  );
}