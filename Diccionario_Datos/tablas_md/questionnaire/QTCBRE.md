# questionnaire.QTCBRE

> Bed Rails And Entrapment Risk Assessment

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Bed Rails And Entrapment Risk Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | Patient assessment |
| Q10 | varchar |  |  | SI | Do the risks of using bed rails outweigh the possi... |
| Q11 | varchar |  |  | SI | If the answer is ''Yes'' to any of the above pleas... |
| Q12 | varchar |  |  | SI | If the patient has been deemed suitable for bed ra... |
| Q13 | varchar |  |  | SI | Adult Entrapment Risk Assessment |
| Q14 | varchar |  |  | SI | Adult entrapment |
| Q15 | varchar |  |  | SI | The checklist should be used in conjunction with c... |
| Q16 | varchar |  |  | SI | Yes responses indicate the desired outcome. |
| Q17 | varchar |  |  | SI | Risk assessments should be carried out before use ... |
| Q18 | varchar |  |  | SI | Is the bed rail to be used with a patient taller t... |
| Q19 | varchar |  |  | SI | Has the bed rail been inspected and maintained reg... |
| Q2 | varchar |  |  | SI | Is it likely that the patient would fall from thei... |
| Q20 | varchar |  |  | SI | Does the manufacturer / supplier provide any infor... |
| Q21 | varchar |  |  | SI | Do you have enough information from the supplier t... |
| Q22 | varchar |  |  | SI | Are the bed rails suitable for the intended bed, a... |
| Q23 | varchar |  |  | SI | Do the fittings or mattress allow the bed rails to... |
| Q24 | varchar |  |  | SI | Does the benefit of any special or extra mattress ... |
| Q25 | varchar |  |  | SI | Does the bed rail height consider any increased ma... |
| Q26 | varchar |  |  | SI | Have you made sure there are no gaps present that ... |
| Q27 | varchar |  |  | SI | Have you made sure there are no gaps between the b... |
| Q28 | varchar |  |  | SI | Have you made sure there are no gaps between the l... |
| Q29 | varchar |  |  | SI | Is the headboard to bed rail end gap appropriate? |
| Q3 | varchar |  |  | SI | Could the risk of falling from bed be reduced by m... |
| Q30 | varchar |  |  | SI | Additional comments |
| Q31 | varchar |  |  | SI | replacement of any part of the equipment combinati... |
| Q32 | date |  |  | SI | Date |
| Q33 | time |  |  | SI | Time |
| Q34 | varchar |  |  | SI |  If any ''No'' response has been selected, there m... |
| Q35 | varchar |  |  | SI | Changes to consider are patient condition, equipme... |
| Q36 | varchar |  |  | SI | Have you made sure there are no gaps between the b... |
| Q37 | varchar |  |  | SI | Have you made sure there are no gaps between the b... |
| Q38 | varchar |  |  | SI | Additional comments |
| Q39 | varchar |  |  | SI | If the answer is Yes to any of the above please st... |
| Q4 | varchar |  |  | SI | Could the use of bed rails increase risks to the p... |
| Q5 | varchar |  |  | SI | Is the patient likely to try and get out of bed or... |
| Q6 | varchar |  |  | SI | Has the patient been assessed for the use of bed r... |
| Q7 | varchar |  |  | SI | Is the configuration of bed, mattress and rail sys... |
| Q8 | varchar |  |  | SI | Has interaction with other equipment (e.g. hoists)... |
| Q9 | varchar |  |  | SI | Has interaction with the work environment (e.g. re... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*