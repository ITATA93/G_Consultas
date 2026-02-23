# SQLUser.MRC_HabitsQuantity

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QTY_ParRef | bigint | PK |  | NO | MRC_Habits Parent Reference |
| Q01 | - |  |  | SI | ¿Mantiene limpios y sin obstáculos los suelos y la... |
| Q02 | - |  |  | SI | ¿Están bien fijos al suelo los bordes de las alfom... |
| Q03 | - |  |  | SI | ¿Tiene desniveles en el suelo dentro de su casa? |
| Q04 | - |  |  | SI | ¿Puede moverse de un lugar a otro de la casa libre... |
| Q05 | - |  |  | SI | ¿Tiene cables en el suelo de los pasillos? |
| Q06 | - |  |  | SI | ¿Usa goma antideslizante en el piso de la tina o d... |
| Q07 | - |  |  | SI | ¿Puede alcanzar fácilmente el jabón y las toallas ... |
| Q08 | - |  |  | SI | ¿Usa cortina en la tina o ducha? |
| Q09 | - |  |  | SI | ¿Tiene el interruptor del baño cerca de la puerta? |
| Q10 | - |  |  | SI | ¿Los interruptores para encender la luz están cerc... |
| Q11 | - |  |  | SI | ¿La iluminación de la casa es la suficiente para v... |
| Q12 | - |  |  | SI | ¿Tiene interruptor para encender la luz al princip... |
| Q13 | - |  |  | SI | ¿Tiene barandas o pasamanos a ambos lados de la es... |
| Q14 | - |  |  | SI | ¿Están las escaleras en buen estado? |
| Q15 | - |  |  | SI | ¿Es fácil de subir su escalera? |
| Q16 | - |  |  | SI | ¿Usa usted una silla firme y fuerte para alcanzar ... |
| Q17 | - |  |  | SI | ¿Están todas sus sillas en buen estado? |
| Q18 | - |  |  | SI | ¿Coloca los utensilios más usados de la cocina, en... |
| Q19 | - |  |  | SI | ¿Se preocupa del encendido y apagado de la cocina? |
| Q20 | - |  |  | SI | ¿Sus zapatos tienen una suela firme y que no se re... |
| Q21 | - |  |  | SI | ¿Utiliza zapatos cómodos y que no se salgan de los... |
| QTY_Childsub | double |  |  | NO | Childsub |
| QTY_Code | varchar |  |  | NO | Code |
| QTY_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| QTY_CreatedDate | date |  |  | SI | Created Date |
| QTY_CreatedTime | time |  |  | SI | Created Time |
| QTY_CreatedUser_DR | bigint |  | FK | SI | Created User |
| QTY_DateFrom | date |  |  | SI | Date From |
| QTY_DateTo | date |  |  | SI | Date To |
| QTY_Desc | varchar |  |  | NO | Description |
| QTY_RowId | varchar |  |  | NO | - |
| QTY_UpdatedDate | date |  |  | SI | Updated Date |
| QTY_UpdatedTime | time |  |  | SI | Updated Time |
| QTY_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
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