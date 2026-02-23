# SQLUser.PA_CumDoseHist

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIST_ParRef | varchar | PK |  | NO | PA_CumDose Parent Reference |
| HIST_Childsub | double |  |  | NO | Childsub |
| HIST_Date | date |  |  | SI | Date |
| HIST_DoseVal | double |  |  | SI | Dose Value Given, Dose Value per Max UOM  |
| HIST_DoseValOtherUOM | double |  |  | SI | Dose Value Given in Other UPM
if the UOM of the d... |
| HIST_Medication_DR | varchar |  | FK | SI | Des Ref MRMedication |
| HIST_OrdExec_DR | varchar |  | FK | SI | Des Ref OEOrdExec |
| HIST_OtherUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| HIST_RowId | varchar |  |  | NO | - |
| HIST_Time | time |  |  | SI | Time  |
| Q01 | - |  |  | SI | Fecha destete |
| Q02 | - |  |  | SI | Hora destete |
| Q03 | - |  |  | SI | ¿Heces blandas y acuosas? |
| Q04 | - |  |  | SI | ¿Vómitos / arcadas / náuseas? |
| Q05 | - |  |  | SI | ¿Temperatura sobre 37,8? |
| Q06 | - |  |  | SI | Estado |
| Q07 | - |  |  | SI | Temblor |
| Q08 | - |  |  | SI | Cualquier sudoración |
| Q09 | - |  |  | SI | Movimientos anormales o repetitivos |
| Q10 | - |  |  | SI | Bostezos o estornudos |
| Q11 | - |  |  | SI | Sobresalto al tocar |
| Q12 | - |  |  | SI | Tono muscular |
| Q13 | - |  |  | SI | Tiempo hasta que se calma (SBS* igual o menor a 1) |
| Q14 | - |  |  | SI | Inicie la puntuación WAT-1 desde el primer día del... |
| Q15 | - |  |  | SI | Continúe anotando dos veces al día hasta 72 horas ... |
| Q16 | - |  |  | SI | WAT-1 debe completarse en conjunto con SBS * al me... |
| Q17 | - |  |  | SI | El estímulo progresivo utilizado en la evaluación ... |
| Q18 | - |  |  | SI | Obtenga información del registro del paciente (est... |
| Q19 | - |  |  | SI | Heces blandas / acuosas: Puntúe 1 si se documentar... |
| Q20 | - |  |  | SI | Vómitos / arcadas / náuseas: Puntuación 1 si se do... |
| Q21 | - |  |  | SI | Temperatura> 37,8 ° C: puntuación 1 si la temperat... |
| Q22 | - |  |  | SI | Observaciones 2 minutos pre estimulación: |
| Q23 | - |  |  | SI | Estado: Puntúe 1 si está despierto y se observa an... |
| Q24 | - |  |  | SI | Temblor: Puntúe 1 si se observa un temblor de mode... |
| Q25 | - |  |  | SI | Sudoración: Puntúe 1 si hay sudoración durante los... |
| Q26 | - |  |  | SI | Movimientos anormales o repetitivos: Puntúe 1 si s... |
| Q27 | - |  |  | SI | agitar las piernas o los brazos o arquear el torso... |
| Q28 | - |  |  | SI | Bostezos o estornudo s> 1: Puntuación 1 si se obse... |
| Q29 | - |  |  | SI | Observaciones 1 minuto post estimulación: |
| Q30 | - |  |  | SI | Sobresalto al tocar: Puntúe 1 si se produce un sob... |
| Q31 | - |  |  | SI | Tono muscular: Puntúe 1 si el tono aumentó durante... |
| Q32 | - |  |  | SI | Recuperación posterior al estímulo: |
| Q33 | - |  |  | SI | Tiempo para recuperar el estado de calma (SBS1 $ 0... |
| Q34 | - |  |  | SI | Sume los 11 números de la columna para obtener el ... |
| Q35 | - |  |  | SI | *= State Behavioural Scale |
| Q36 | - |  |  | SI | Puntaje |
| Q37 | - |  |  | SI | Clasificación |
| Q38 | - |  |  | SI | 0 - 12 |
| Q39 | - |  |  | SI | Una puntuación WAT-1 más alta indica más síntomas ... |
| Q40 | - |  |  | SI | WAT-1 es una escala de 11 ítems / 12 puntos para m... |
| Q41 | - |  |  | SI | 0 - 12: Una puntuación WAT-1 más alta indica más s... |
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