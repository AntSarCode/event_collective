export default function SocialBar({ fb, ig, tt }:{fb?:string; ig?:string; tt?:string}) {
  return (
    <div className="pl-24 md:pl-32 py-6 flex gap-6 opacity-80">
      {fb ? <a href={fb} aria-label="Facebook">FB</a> : null}
      {ig ? <a href={ig} aria-label="Instagram">IG</a> : null}
      {tt ? <a href={tt} aria-label="TikTok">TT</a> : null}
    </div>
  );
}
