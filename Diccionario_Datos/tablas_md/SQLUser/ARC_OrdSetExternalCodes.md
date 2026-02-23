# SQLUser.ARC_OrdSetExternalCodes

**Schema:** SQLUser
**Columnas:** 133
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EX_ParRef | varchar | PK |  | NO | ARC_OrdSets Parent Reference |
| EX_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| EX_Childsub | double |  |  | NO | Childsub |
| EX_Code | varchar |  |  | SI | Code |
| EX_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EX_CreatedDate | date |  |  | SI | Created Date |
| EX_CreatedTime | time |  |  | SI | Created Time |
| EX_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EX_DateFrom | date |  |  | SI | Date From |
| EX_DateTo | date |  |  | SI | Date To |
| EX_Desc | varchar |  |  | SI | Description |
| EX_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| EX_RowId | varchar |  |  | NO | - |
| EX_UpdatedDate | date |  |  | SI | Updated Date |
| EX_UpdatedTime | time |  |  | SI | Updated Time |
| EX_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | INSTRUMENTO DIAGNOSTICO MUJERES VICTIMAS VIOLENCIA... |
| Q02 | - |  |  | SI | I. Diagnóstico de Mujeres Víctimas de Violencia de... |
| Q03 | - |  |  | SI | Ahora le preguntaré sobre algunas situaciones que ... |
| Q04 | - |  |  | SI | Control en la Relación y Violencia Psicológica |
| Q05 | - |  |  | SI | ¿Trata de impedir que vea a sus amistades? |
| Q06 | - |  |  | SI | Frecuencia |
| Q07 | - |  |  | SI | ¿Trata de restringir el contacto con su familia? |
| Q08 | - |  |  | SI | Frecuencia |
| Q09 | - |  |  | SI | ¿Insiste en saber dónde está usted en todo momento... |
| Q10 | - |  |  | SI | Frecuencia |
| Q11 | - |  |  | SI | ¿La ignora o la trata de manera indiferente? |
| Q12 | - |  |  | SI | Frecuencia |
| Q13 | - |  |  | SI | ¿Se molesta si usted habla con otro hombre? |
| Q14 | - |  |  | SI | Frecuencia |
| Q15 | - |  |  | SI | ¿Sospecha a menudo que usted le es infiel? |
| Q16 | - |  |  | SI | Frecuencia |
| Q17 | - |  |  | SI | ¿Usted tiene que pedirle permiso antes de buscar a... |
| Q18 | - |  |  | SI | Frecuencia |
| Q19 | - |  |  | SI | ¿La insulta o la hace sentir mal con usted misma? |
| Q20 | - |  |  | SI | Frecuencia |
| Q21 | - |  |  | SI | ¿La menosprecia o humilla frente a otras personas? |
| Q22 | - |  |  | SI | Frecuencia |
| Q23 | - |  |  | SI | ¿Hace cosas a propósito para asustarla o intimidar... |
| Q24 | - |  |  | SI | Frecuencia |
| Q25 | - |  |  | SI | ¿La amenaza con herirla a usted o a alguien que us... |
| Q26 | - |  |  | SI | Frecuencia |
| Q27 | - |  |  | SI | N° Respuestas Si |
| Q28 | - |  |  | SI | Puntaje |
| Q29 | - |  |  | SI | Psicológica |
| Q30 | - |  |  | SI | Violencia Física |
| Q31 | - |  |  | SI | Su esposo o pareja la |
| Q32 | - |  |  | SI | ¿Abofetea o le tira cosas que pudieran herirla? |
| Q33 | - |  |  | SI | Frecuencia |
| Q34 | - |  |  | SI | ¿Empuja, zamarrea, arrincona o le tira el pelo? |
| Q35 | - |  |  | SI | Frecuencia |
| Q36 | - |  |  | SI | ¿Golpea con puño o con alguna otra cosa que pudier... |
| Q37 | - |  |  | SI | Frecuencia |
| Q38 | - |  |  | SI | ¿Patea, la arrastra o le ha dado una golpiza? |
| Q39 | - |  |  | SI | Frecuencia |
| Q40 | - |  |  | SI | ¿Intentado estrangular? |
| Q41 | - |  |  | SI | Frecuencia |
| Q42 | - |  |  | SI | ¿Intentado quemarla o quemado? |
| Q43 | - |  |  | SI | Frecuencia |
| Q44 | - |  |  | SI | ¿Amenazada con usar, a usado una pistola, cuchillo... |
| Q45 | - |  |  | SI | Frecuencia |
| Q46 | - |  |  | SI | N° Respuestas Si |
| Q47 | - |  |  | SI | Puntaje |
| Q48 | - |  |  | SI | Violencia Sexual |
| Q49 | - |  |  | SI | Su pareja o esposo |
| Q50 | - |  |  | SI | 1-¿La descalificó en su sexualidad, o su cuerpo, c... |
| Q51 | - |  |  | SI | Frecuencia |
| Q52 | - |  |  | SI | 2-¿La forzó alguna vez a realizar algún acto sexua... |
| Q53 | - |  |  | SI | Frecuencia |
| Q54 | - |  |  | SI | 3-¿Quiso que usted tuviera relaciones sexuales cua... |
| Q55 | - |  |  | SI | Frecuencia |
| Q56 | - |  |  | SI | 4-¿La ha forzado físicamente a tener relaciones se... |
| Q57 | - |  |  | SI | N° Respuestas Si |
| Q58 | - |  |  | SI | Puntaje |
| Q59 | - |  |  | SI | Violencia Económica |
| Q60 | - |  |  | SI | ¿Usted tiene que rendirle cuentas de todo lo que g... |
| Q61 | - |  |  | SI | Frecuencia |
| Q62 | - |  |  | SI | ¿Usted debe darle todo o una parte del dinero a su... |
| Q63 | - |  |  | SI | Frecuencia |
| Q64 | - |  |  | SI | ¿Alguna vez usted ha dejado, rechazado un trabajo ... |
| Q65 | - |  |  | SI | Frecuencia |
| Q66 | - |  |  | SI | ¿Alguna vez su esposo o pareja ha tomado su dinero... |
| Q67 | - |  |  | SI | Frecuencia |
| Q68 | - |  |  | SI | ¿Su esposo o pareja se ha negado alguna vez a darl... |
| Q69 | - |  |  | SI | Frecuencia |
| Q70 | - |  |  | SI | N° Respuestas Si |
| Q71 | - |  |  | SI | Puntaje |
| Q72 | - |  |  | SI | Física |
| Q73 | - |  |  | SI | Sexual |
| Q74 | - |  |  | SI | Económica |
| Q75 | - |  |  | SI | II. Data de la Violencia |
| Q76 | - |  |  | SI | ¿Desde hace cuánto tiempo o años que la situación ... |
| Q77 | - |  |  | SI | Frecuencia |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*