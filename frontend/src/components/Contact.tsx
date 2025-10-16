import { Mail, Phone } from "lucide-react";

export const Contact = () => {
  return (
    <section className="py-20 bg-secondary/30">
      <div className="container mx-auto px-4">
        <div className="text-center mb-12">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground mb-4">
            Get in <span className="text-primary">Touch</span>
          </h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Have questions? We're here to help you on your learning journey
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto">
          <div className="bg-card p-8 rounded-lg shadow-lg text-center hover:shadow-xl transition-shadow">
            <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
              <Mail className="h-8 w-8 text-primary" />
            </div>
            <h3 className="text-xl font-semibold text-foreground mb-2">Support</h3>
            <a 
              href="mailto:support@iqvara.com" 
              className="text-muted-foreground hover:text-primary transition-colors"
            >
              support@iqvara.com
            </a>
          </div>

          <div className="bg-card p-8 rounded-lg shadow-lg text-center hover:shadow-xl transition-shadow">
            <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
              <Mail className="h-8 w-8 text-primary" />
            </div>
            <h3 className="text-xl font-semibold text-foreground mb-2">General Contact</h3>
            <a 
              href="mailto:contact@iqvara.com" 
              className="text-muted-foreground hover:text-primary transition-colors"
            >
              contact@iqvara.com
            </a>
          </div>

          <div className="bg-card p-8 rounded-lg shadow-lg text-center hover:shadow-xl transition-shadow">
            <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
              <Phone className="h-8 w-8 text-primary" />
            </div>
            <h3 className="text-xl font-semibold text-foreground mb-2">Phone</h3>
            <a 
              href="tel:+1234567890" 
              className="text-muted-foreground hover:text-primary transition-colors"
            >
              +1 (234) 567-890
            </a>
          </div>
        </div>
      </div>
    </section>
  );
};
