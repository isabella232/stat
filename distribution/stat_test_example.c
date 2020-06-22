/**
* @file
* 
* @copyright Copyright (c) 2020 Western Digital Corporation or its affiliates,
*
* @project   STAT Framework
* @date      July 31, 2016
* @brief     Implements an example test main-file
*******************************************************************************/

/******************************************************************************/
/*     INCLUDE FILES                                                          */
/******************************************************************************/
#include <stat.h>
#include "dummy_header.h"

/******************************************************************************/
/*     DEFINITIONS                                                            */
/******************************************************************************/
#if !defined(D_TEST_EXAMPLE) || !defined(D_TEST_EXAMPLE)
#error "Example mak-file has been corrupted!"
#endif

/******************************************************************************/
/*     MACROS                                                                 */
/******************************************************************************/

/******************************************************************************/
/*     TYPES                                                                  */
/******************************************************************************/

/******************************************************************************/
/*     LOCAL PROTOTYPES                                                       */
/******************************************************************************/

/******************************************************************************/
/*     EXTERNAL PROTOTYPES                                                    */
/******************************************************************************/

/******************************************************************************/
/*     GLOBAL VARIABLES                                                       */
/******************************************************************************/

/******************************************************************************/
/*     START IMPLEMENTATION                                                   */
/******************************************************************************/

/**
* Implements the user main routine that shall be implemented in every STAT 
* package
*
* @return status depicting success or failure returned by the Unity harness
* @remarks Shall be implemented in every STAT package
*/
_UU32 Stat_Main(void)
{
  UNITY_BEGIN();
  return UNITY_END();
}

/******************************************************************************/
/**    END OF FILE                                                           **/
/******************************************************************************/

