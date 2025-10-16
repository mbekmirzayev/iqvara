import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { GraduationCap } from "lucide-react";

export const Header = () => {
  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center justify-between">
        <Link to="/" className="flex items-center gap-2 font-bold text-2xl">
          <GraduationCap className="h-8 w-8 text-primary" />
          <span className="bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">
            Iqvara
          </span>
        </Link>
        
        <nav className="flex items-center gap-6">
          <Link to="/careers" className="text-sm font-medium text-foreground/80 hover:text-primary transition-colors">
            Careers
          </Link>
          <Link to="/courses" className="text-sm font-medium text-foreground/80 hover:text-primary transition-colors">
            Courses
          </Link>
          <Link to="/blogs" className="text-sm font-medium text-foreground/80 hover:text-primary transition-colors">
            Blogs
          </Link>
          <Link to="/faq" className="text-sm font-medium text-foreground/80 hover:text-primary transition-colors">
            FAQ
          </Link>
          <Link to="/login">
            <Button variant="outline" size="sm">Login</Button>
          </Link>
        </nav>
      </div>
    </header>
  );
};
