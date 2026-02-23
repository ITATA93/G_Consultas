# SQLUser.ARC_InsTypeDRGBaseRate

**Schema:** SQLUser
**Columnas:** 123
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRGBR_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| DRGBR_ApplyEpisodeDateDRGCost | varchar |  |  | SI | Apply Episode Date for DRG Cost |
| DRGBR_ApplySurgHighCost | varchar |  |  | SI | Apply Surgical High Cost Calculation  |
| DRGBR_BaseRate | double |  |  | SI | Base Rate |
| DRGBR_Childsub | double |  |  | NO | Childsub |
| DRGBR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRGBR_CreatedDate | date |  |  | SI | Created Date |
| DRGBR_CreatedTime | time |  |  | SI | Created Time |
| DRGBR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRGBR_DRGCostTariff_DR | bigint |  | FK | SI | DRG Cost Tariff, Des Ref ARCTariff |
| DRGBR_DRGGap | double |  |  | SI | DRG Gap |
| DRGBR_DRGMargin | double |  |  | SI | DRG Margin |
| DRGBR_DateFrom | date |  |  | SI | Date From |
| DRGBR_DateTo | date |  |  | SI | Date To |
| DRGBR_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| DRGBR_HighOutlierMedARCIM_DR | varchar |  | FK | SI | High Outlier Medical, Des Ref ARCItmMast |
| DRGBR_HighOutlierProcARCIM_DR | varchar |  | FK | SI | High Outlier Procedural, Des Ref ARCItmMast |
| DRGBR_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| DRGBR_LTCARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| DRGBR_LowOutlierARCIM_DR | varchar |  | FK | SI | Low Outlier, Des Ref ARCItmMast |
| DRGBR_OutlierARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| DRGBR_OutlierDiscMed | double |  |  | SI | Outlier Discount - Medical |
| DRGBR_OutlierDiscSurg | double |  |  | SI | Outlier Discount - Surgical |
| DRGBR_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| DRGBR_RowId | varchar |  |  | NO | - |
| DRGBR_SplitPayorPerc | double |  |  | SI | Split Payor Percentage |
| DRGBR_TransHighOutlierARCIM_DR | varchar |  | FK | SI | Transfer High Outlier, Des Ref ARCItmMast |
| DRGBR_TransLowOutlierARCIM_DR | varchar |  | FK | SI | Transfer Low Outlier, Des Ref ARCItmMast |
| DRGBR_UpdatedDate | date |  |  | SI | Updated Date |
| DRGBR_UpdatedTime | time |  |  | SI | Updated Time |
| DRGBR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | fecha de vigencia EMPA |
| Q02 | - |  |  | SI | Audit |
| Q03 | - |  |  | SI | Realiza ejercicio |
| Q04 | - |  |  | SI | Fumador |
| Q05 | - |  |  | SI | Se ha sentido triste, deprimida o pesimista casi t... |
| Q06 | - |  |  | SI | Siente que ya no disfruta o ha perdido el interés |
| Q07 | - |  |  | SI | ¿Duran los síntomas más de dos semanas? |
| Q08 | - |  |  | SI | Peso |
| Q08ObsDR | - |  |  | SI | Peso DR |
| Q09 | - |  |  | SI | Talla |
| Q09ObsDR | - |  |  | SI | Talla DR |
| Q10 | - |  |  | SI | IMC |
| Q11 | - |  |  | SI | Circunferencia cintura |
| Q11ObsDR | - |  |  | SI | Circunferencia cintura DR |
| Q12 | - |  |  | SI | Talla Máxima Registrada |
| Q13 | - |  |  | SI | Pérdida de Estatura > 7 cm |
| Q14 | - |  |  | SI | Estado Nutricional |
| Q14ObsDR | - |  |  | SI | Estado Nutricional  DR |
| Q15 | - |  |  | SI | Presión Arterial Sistólica Actual |
| Q15ObsDR | - |  |  | SI | Presión Arterial Sistólica Actual  DR |
| Q16 | - |  |  | SI | Presión Arterial Diastólica Actual |
| Q16ObsDR | - |  |  | SI | Presión Arterial Diastólica Actual  DR |
| Q17 | - |  |  | SI | Colesterol Total Actual |
| Q17ObsDR | - |  |  | SI | Colesterol Total Actual DR |
| Q18 | - |  |  | SI | Colesterol HDL Actual |
| Q18ObsDR | - |  |  | SI | Colesterol HDL Actual DR |
| Q19 | - |  |  | SI | Triglicéridos Actual |
| Q19ObsDR | - |  |  | SI | Triglicéridos Actual  DR |
| Q20 | - |  |  | SI | Glicemia Actual |
| Q20ObsDR | - |  |  | SI | Glicemia Actual  DR |
| Q21 | - |  |  | SI | Riesgo Cardiovascular ATP III |
| Q22 | - |  |  | SI | Ha tenido tos productiva por más de 15 días |
| Q23 | - |  |  | SI | V.D.R.L |
| Q23ObsDR | - |  |  | SI | V.D.R.L DR |
| Q24 | - |  |  | SI | R.P.R |
| Q24ObsDR | - |  |  | SI | R.P.R DR |
| Q25 | - |  |  | SI | Requiere VIH |
| Q26 | - |  |  | SI | Prevención de cáncer cérvico-uterino |
| Q27 | - |  |  | SI | Fecha examen |
| Q28 | - |  |  | SI | Diagnóstico Primario |
| Q29 | - |  |  | SI | Descripción de calidad de la muestra |
| Q30 | - |  |  | SI | Diagnósticos Secundarios |
| Q31 | - |  |  | SI | Descripción de Sugerencias |
| Q32 | - |  |  | SI | Fecha Próximo PAP |
| Q33 | - |  |  | SI | Mamografía |
| Q34 | - |  |  | SI | Fecha de registro mamografía |
| Q35 | - |  |  | SI | Mamografía |
| Q36 | - |  |  | SI | Conducta a seguir |
| Q37 | - |  |  | SI | Fecha de próxima mamografía |
| Q38 | - |  |  | SI | Observaciones |
| Q39 | - |  |  | SI | Plan |
| Q40 | - |  |  | SI | Estado del EMPA |
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