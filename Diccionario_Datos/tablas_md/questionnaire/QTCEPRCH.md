# questionnaire.QTCEPRCH

> Pauta de Evaluación de Riesgo de Caídas en el Hogar y Entorno Comunitario

**Schema:** questionnaire
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pauta de Evaluación de Riesgo de Caídas en el Hogar y Entorno Comunitario

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | ¿Mantiene limpios y sin obstáculos los suelos y la... |
| Q02 | varchar |  |  | SI | ¿Están bien fijos al suelo los bordes de las alfom... |
| Q03 | varchar |  |  | SI | ¿Tiene desniveles en el suelo dentro de su casa? |
| Q04 | varchar |  |  | SI | ¿Puede moverse de un lugar a otro de la casa libre... |
| Q05 | varchar |  |  | SI | ¿Tiene cables en el suelo de los pasillos? |
| Q06 | varchar |  |  | SI | ¿Usa goma antideslizante en el piso de la tina o d... |
| Q07 | varchar |  |  | SI | ¿Puede alcanzar fácilmente el jabón y las toallas ... |
| Q08 | varchar |  |  | SI | ¿Usa cortina en la tina o ducha? |
| Q09 | varchar |  |  | SI | ¿Tiene el interruptor del baño cerca de la puerta? |
| Q10 | varchar |  |  | SI | ¿Los interruptores para encender la luz están cerc... |
| Q11 | varchar |  |  | SI | ¿La iluminación de la casa es la suficiente para v... |
| Q12 | varchar |  |  | SI | ¿Tiene interruptor para encender la luz al princip... |
| Q13 | varchar |  |  | SI | ¿Tiene barandas o pasamanos a ambos lados de la es... |
| Q14 | varchar |  |  | SI | ¿Están las escaleras en buen estado? |
| Q15 | varchar |  |  | SI | ¿Es fácil de subir su escalera? |
| Q16 | varchar |  |  | SI | ¿Usa usted una silla firme y fuerte para alcanzar ... |
| Q17 | varchar |  |  | SI | ¿Están todas sus sillas en buen estado? |
| Q18 | varchar |  |  | SI | ¿Coloca los utensilios más usados de la cocina, en... |
| Q19 | varchar |  |  | SI | ¿Se preocupa del encendido y apagado de la cocina? |
| Q20 | varchar |  |  | SI | ¿Sus zapatos tienen una suela firme y que no se re... |
| Q21 | varchar |  |  | SI | ¿Utiliza zapatos cómodos y que no se salgan de los... |
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