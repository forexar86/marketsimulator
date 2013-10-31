/** Beta distribution
 *
 * Conditions on the parameters are |alpha| > 0 and |beta| > 0.
 * Returned values range between 0 and 1.
 */
@python.random
def betavariate(Alpha : Float = 1.0, Beta : Float = 1.0)

/** Exponential distribution
 *
 * |lambda| is 1.0 divided by the desired mean.
 * It should be greater zero. Returned values range from 0 to positive infinity
 */
@python.random
def expovariate(Lambda : Float = 1.0)

/** Uniform distribution
 *
 * Return a random floating point number *N* such that
 * *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
 * The end-point value *b* may or may not be included in the range depending on
 * floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
 */
@python.random
def uniform(Low : Float = -10.0, High : Float = 10.0)

/** Triangular distribution
  *
  * Return a random floating point number *N* such that *low* <= *N* <= *high* and
  *       with the specified *mode* between those bounds.
  *       The *low* and *high* bounds default to zero and one.
  *       The *mode* argument defaults to the midpoint between the bounds,
  *       giving a symmetric distribution.
  */
@python.random
def triangular(Low : Float = 0.0, High : Float = 1.0, Mode : Float = 0.5)

/** Gamma distribution
 *
 *  Conditions on the parameters are |alpha| > 0 and |beta| > 0.
 *
 *  The probability distribution function is: ::
 *
 *               x ** (alpha - 1) * math.exp(-x / beta)
 *     pdf(x) =  --------------------------------------
 *                  math.gamma(alpha) * beta ** alpha
 */
@python.random
def gammavariate(Alpha : Float = 1.0, Beta : Float = 1.0)

/** Log normal distribution
 *
 * If you take the natural logarithm of this distribution,
 *  you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
 *  |mu| can have any value, and |sigma| must be greater than zero.
 */
@python.random
def lognormvariate(Mu : Float = 0.0, Sigma : Float = 1.0)

/** Normal distribution
 *
 *  |mu| is the mean, and |sigma| is the standard deviation.
 */
@python.random
def normalvariate(Mu : Float = 0.0, Sigma : Float = 1.0)

/** Von Mises distribution
 *
 *  |mu| is the mean angle, expressed in radians between 0 and 2|pi|,
 *      and |kappa| is the concentration parameter, which must be greater than or equal to zero.
 *      If |kappa| is equal to zero, this distribution reduces
 *      to a uniform random angle over the range 0 to 2|pi|
 */
@python.random
def vonmisesvariate(Mu : Float = 0.0, Kappa : Float = 0.0)

/** Pareto distribution
 *
 *  |alpha| is the shape parameter.
 */
@python.random
def paretovariate(Alpha : Float = 1.0)

/** Weibull distribution
 *
 *  |alpha| is the scale parameter and |beta| is the shape parameter
 */
@python.random
def weibullvariate(Alpha : Float = 1.0, Beta : Float = 1.0)


 ->
/** Beta distribution
 *
 * Conditions on the parameters are |alpha| > 0 and |beta| > 0.
 * Returned values range between 0 and 1.
 */
@python.random()
def betavariate(Alpha : Float = 1.0, Beta : Float = 1.0)

/** Exponential distribution
 *
 * |lambda| is 1.0 divided by the desired mean.
 * It should be greater zero. Returned values range from 0 to positive infinity
 */
@python.random()
def expovariate(Lambda : Float = 1.0)

/** Uniform distribution
 *
 * Return a random floating point number *N* such that
 * *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
 * The end-point value *b* may or may not be included in the range depending on
 * floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
 */
@python.random()
def uniform(Low : Float = -10.0, High : Float = 10.0)

/** Triangular distribution
 *
 * Return a random floating point number *N* such that *low* <= *N* <= *high* and
 *       with the specified *mode* between those bounds.
 *       The *low* and *high* bounds default to zero and one.
 *       The *mode* argument defaults to the midpoint between the bounds,
 *       giving a symmetric distribution.
 */
@python.random()
def triangular(Low : Float = 0.0, High : Float = 1.0, Mode : Float = 0.5)

/** Gamma distribution
 *
 *  Conditions on the parameters are |alpha| > 0 and |beta| > 0.
 *
 *  The probability distribution function is: ::
 *
 *               x ** (alpha - 1) * math.exp(-x / beta)
 *     pdf(x) =  --------------------------------------
 *                  math.gamma(alpha) * beta ** alpha
 */
@python.random()
def gammavariate(Alpha : Float = 1.0, Beta : Float = 1.0)

/** Log normal distribution
 *
 * If you take the natural logarithm of this distribution,
 *  you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
 *  |mu| can have any value, and |sigma| must be greater than zero.
 */
@python.random()
def lognormvariate(Mu : Float = 0.0, Sigma : Float = 1.0)

/** Normal distribution
 *
 *  |mu| is the mean, and |sigma| is the standard deviation.
 */
@python.random()
def normalvariate(Mu : Float = 0.0, Sigma : Float = 1.0)

/** Von Mises distribution
 *
 *  |mu| is the mean angle, expressed in radians between 0 and 2|pi|,
 *      and |kappa| is the concentration parameter, which must be greater than or equal to zero.
 *      If |kappa| is equal to zero, this distribution reduces
 *      to a uniform random angle over the range 0 to 2|pi|
 */
@python.random()
def vonmisesvariate(Mu : Float = 0.0, Kappa : Float = 0.0)

/** Pareto distribution
 *
 *  |alpha| is the shape parameter.
 */
@python.random()
def paretovariate(Alpha : Float = 1.0)

/** Weibull distribution
 *
 *  |alpha| is the scale parameter and |beta| is the shape parameter
 */
@python.random()
def weibullvariate(Alpha : Float = 1.0, Beta : Float = 1.0)

