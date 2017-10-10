class EndOfPathException: public exception
{
  virtual const char* what() const throw()
  {
    return "My exception happened";
  }
} myex;
