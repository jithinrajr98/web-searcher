export interface Source {
  title: string;
  url: string;
}

export interface ResearchResponse {
  query: string;
  report: string;
  sources: Source[];
}
