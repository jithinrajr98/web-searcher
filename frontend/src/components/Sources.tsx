import type { Source } from "../types";

interface Props {
  sources: Source[];
}

export default function Sources({ sources }: Props) {
  if (sources.length === 0) return null;

  return (
    <section className="sources">
      <h2>Sources</h2>
      <ol>
        {sources.map((s, i) => (
          <li key={i}>
            <a href={s.url} target="_blank" rel="noopener noreferrer">
              {s.title || s.url}
            </a>
          </li>
        ))}
      </ol>
    </section>
  );
}
