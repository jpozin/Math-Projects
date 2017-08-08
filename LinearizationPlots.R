plot6 <- function(xvar, yvar, dotcol=2, bgcol="papayawhip"){
  #Plots 6 common functions of a graph in order to help the user
  #Identify which plot is the most linear.
  #xvar = explanatory variable
  #yvar = dependent variable
  #dotcol = dot color (default 2 for red)
  #bgcol = background color (default "papayawhip")
  par(mfrow=c(2,3), bg=bgcol)
  plot(xvar, yvar, col=dotcol)
  abline(lm(yvar~xvar))
  plot(xvar^2, yvar, col=dotcol)
  abline(lm(yvar~I(xvar^dotcol)))
  plot(sqrt(xvar), yvar, col=dotcol)
  abline(lm(yvar~I(xvar^0.5)))
  plot(log(xvar), yvar, col=dotcol)
  abline(lm(yvar~log(xvar)))
  plot(xvar^-1, yvar, col=dotcol)
  abline(lm(yvar~I(xvar^-1)))
  plot(xvar^-0.5, yvar, col=dotcol)
  abline(lm(yvar~I(xvar^-0.5)))
}

plot8 <- function(xvar, yvar, dotcol=2, bgcol="papayawhip"){
  #Plots 8 common functions of a graph in order to help the user
  #Identify which trend is the most linear and determine an appropriate data tranformation.
  #xvar = explanatory variable
  #yvar = dependent variable
  #dotcol = dot color (default 2 for red)
  #bgcol = background color (default "papayawhip")
  par(mfrow=c(2,4), bg=bgcol)
  plot(xvar, yvar, col=dotcol)
  abline(lm(yvar~xvar))
  plot(xvar^dotcol, yvar, col=dotcol)
  abline(lm(yvar~I(xvar^2)))
  plot(sqrt(xvar), yvar, col=dotcol)
  abline(lm(yvar~I(xvar^0.5)))
  plot(log(xvar), yvar, col=dotcol)
  abline(lm(yvar~log(xvar)))
  plot(xvar^-1, yvar, col=dotcol)
  abline(lm(yvar~I(xvar^-1)))
  plot(xvar^-0.5, yvar, col=dotcol)
  abline(lm(yvar~I(xvar^-0.5)))
  plot(exp(xvar), yvar, col=dotcol)
  abline(lm(yvar~I(exp(xvar))))
  plot(1/exp(xvar), yvar, col=dotcol)
  abline(yvar, I(exp(xvar)^-1))
}