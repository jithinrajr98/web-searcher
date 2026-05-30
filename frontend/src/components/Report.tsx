import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";

interface Props {
  report: string;
}

export default function Report({ report }: Props) {
  return (
    <article className="report">
      <Markdown remarkPlugins={[remarkGfm]}>{report}</Markdown>
    </article>
  );
}
