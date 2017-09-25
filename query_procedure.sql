CREATE OR REPLACE PROCEDURE DRUGO73.DELETEBASTIDORESFF (TID IN INTEGER, BAST IN VARCHAR2) IS
ID_ENCONTRADO NUMBER;
/******************************************************************************
   NAME:       deleteBastidoresFF
   PURPOSE:    

   REVISIONS:
   Ver        Date        Author           Description
   ---------  ----------  ---------------  ------------------------------------
   1.0        24/09/2017   Israel       1. Created this procedure.

   NOTES:

   Automatically available Auto Replace Keywords:
      Object Name:     deleteBastidoresFF
      Sysdate:         24/09/2017
      Date and Time:   24/09/2017, 16:17:43, and 24/09/2017 16:17:43
      Username:        Israel (set in TOAD Options, Procedure Editor)
      Table Name:       (set in the "New PL/SQL Object" dialog)

******************************************************************************/
BEGIN
       SELECT ID INTO ID_ENCONTRADO FROM DRUGO73.GT_ACTION_PERSONALIZATION_PROX WHERE TRANSACTIONID = TID AND BASTIDOR = BAST;
       IF ID_ENCONTRADO IS NOT NULL THEN   
            DELETE GT_ACTION_PERSONALIZATION_PROX WHERE ID = ID_ENCONTRADO;
       END IF;
       
       EXCEPTION
         WHEN NO_DATA_FOUND THEN
           dbms_output.put_line('NO SE ENCONTRO ID');
         WHEN OTHERS THEN
           -- Consider logging the error and then re-raise
           RAISE;

END deleteBastidoresFF;
/
