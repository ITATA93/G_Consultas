# SQLUser.MRC_ObservationItem

**Schema:** SQLUser
**Columnas:** 190
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_RowId | bigint | PK |  | NO | - |
| ITM_AlertRangeFrom | varchar |  |  | SI | Alert Range From |
| ITM_AlertRangeTo | varchar |  |  | SI | Alert Range To |
| ITM_AlertValueList | varchar |  |  | SI | Alert Value List |
| ITM_AllowMultiple | varchar |  |  | SI | Allow Multiple
Allow multiples of this Observatio... |
| ITM_AlternativeBodyWeight | varchar |  |  | SI | Alternative Body Weight for Prescribing and Admini... |
| ITM_CTUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| ITM_Code | varchar |  |  | NO | Code |
| ITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITM_Confirmation | varchar |  |  | SI | Confirmation |
| ITM_CreatedDate | date |  |  | SI | Created Date |
| ITM_CreatedTime | time |  |  | SI | Created Time |
| ITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITM_CustomType_DR | varchar |  | FK | SI | Custom type |
| ITM_DateFrom | date |  |  | SI | Date From |
| ITM_DateTo | date |  |  | SI | Date To |
| ITM_DecimalPlaces | double |  |  | SI | DecimalPlaces |
| ITM_DefLineColour | varchar |  |  | SI | DefLineColour |
| ITM_DefLineStyle | varchar |  |  | SI | DefLineStyle |
| ITM_DefMarkerShape | varchar |  |  | SI | DefMarkerShape  |
| ITM_DefMarkerSize | varchar |  |  | SI | DefMarkerSize  |
| ITM_DefRefLineColour | varchar |  |  | SI | DefRefLineColour |
| ITM_DefRefLineStyle | varchar |  |  | SI | DefRefLineStyle |
| ITM_Deprecated | bit |  |  | SI | Deprecated |
| ITM_DeprecatedReason | varchar |  |  | SI | Deprecated Reason |
| ITM_Desc | varchar |  |  | NO | Description |
| ITM_DispCTTUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| ITM_FluidBalTotalType | varchar |  |  | SI | ITMFluidBalTotalType |
| ITM_FluidBalanceType | varchar |  |  | SI | Fluid Balance Type |
| ITM_Formula | varchar |  |  | SI | Formula |
| ITM_GraphColor | varchar |  |  | SI | Graph Color |
| ITM_GraphMarker | double |  |  | SI | Graph Marker |
| ITM_GraphPattern | double |  |  | SI | Graph Pattern |
| ITM_HighRange | varchar |  |  | SI | this is an old column and replaced by MRCObservati... |
| ITM_InputType | varchar |  |  | SI | Input Type |
| ITM_IrrigationType | varchar |  |  | SI | Fluid Balance Irrigation Type |
| ITM_Length | double |  |  | SI | Length of Input |
| ITM_LinkedFBItem_DR | bigint |  | FK | SI | Des Ref MRCObservationItem |
| ITM_LowRange | varchar |  |  | SI | this is an old column and replaced by MRCObservati... |
| ITM_MaximumLimit | double |  |  | SI | Maximum numeric value accepted for manual input |
| ITM_MinimumLimit | double |  |  | SI | Minimum numeric value accepted for manual input |
| ITM_ObservStatus_DR | varchar |  | FK | SI | not used |
| ITM_ObservationCategory | bigint |  |  | SI | Observation Category |
| ITM_Owner | varchar |  |  | SI | Owner |
| ITM_Purpose | varchar |  |  | SI | Purpose |
| ITM_RangeFrom | varchar |  |  | SI | Range From |
| ITM_RangeTo | varchar |  |  | SI | Range To |
| ITM_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| ITM_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| ITM_SumAttributeScore | varchar |  |  | SI | Sum of Attribute Scores |
| ITM_SysUOM_DR | bigint |  | FK | SI | Base UOM
System defined Base UOM for System items |
| ITM_System | varchar |  |  | SI | System created |
| ITM_TotalBottleVol | varchar |  |  | SI | Total Bottle Volume Indicator, valid only for Outp... |
| ITM_UpdatedDate | date |  |  | SI | Updated Date |
| ITM_UpdatedTime | time |  |  | SI | Updated Time |
| ITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ITM_ValidActivePregnancyOnly | varchar |  |  | SI | Valid for Active Pregnancy Only |
| ITM_Values | varchar |  |  | SI | Values |
| Q01 | - |  |  | SI | Cereales |
| Q02 | - |  |  | SI | Verduras General |
| Q03 | - |  |  | SI | Verdulas Libre Consumo |
| Q04 | - |  |  | SI | Frutas |
| Q05 | - |  |  | SI | Carnes Altas en Grasas |
| Q06 | - |  |  | SI | Carnes Bajas en Grasas |
| Q07 | - |  |  | SI | Leguminosas |
| Q08 | - |  |  | SI | Lácteos Altos en Grasas |
| Q09 | - |  |  | SI | Lácteos Medios en Grasas |
| Q10 | - |  |  | SI | Lácteos Bajos en Grasas |
| Q11 | - |  |  | SI | Quesillo |
| Q12 | - |  |  | SI | Aceites y Grasas |
| Q13 | - |  |  | SI | Alimentos Ricos en Lípidos |
| Q14 | - |  |  | SI | Azúcar |
| Q15 | - |  |  | SI | Calorias C |
| Q16 | - |  |  | SI | Calorias VG |
| Q17 | - |  |  | SI | Calorias VLC |
| Q18 | - |  |  | SI | Calorias F |
| Q19 | - |  |  | SI | Calorias CAG |
| Q20 | - |  |  | SI | Calorias CBG |
| Q21 | - |  |  | SI | Calorias LG |
| Q22 | - |  |  | SI | Calorias LAG |
| Q23 | - |  |  | SI | Calorias LMG |
| Q24 | - |  |  | SI | Calorias LBG |
| Q25 | - |  |  | SI | Calorias Q |
| Q26 | - |  |  | SI | Calorias AyG |
| Q27 | - |  |  | SI | Calorias ARL |
| Q28 | - |  |  | SI | Calorias AZ |
| Q29 | - |  |  | SI | CHO  C |
| Q30 | - |  |  | SI | CHO  VG |
| Q31 | - |  |  | SI | CHO  VLC |
| Q32 | - |  |  | SI | CHO  F |
| Q33 | - |  |  | SI | CHO  CAG |
| Q34 | - |  |  | SI | CHO  CBG |
| Q35 | - |  |  | SI | CHO  LG |
| Q36 | - |  |  | SI | CHO  LAG |
| Q37 | - |  |  | SI | CHO  LMG |
| Q38 | - |  |  | SI | CHO  LBG |
| Q39 | - |  |  | SI | CHO  Q	 |
| Q40 | - |  |  | SI | CHO  AyG |
| Q41 | - |  |  | SI | CHO  ARL |
| Q42 | - |  |  | SI | CHO  AZ |
| Q43 | - |  |  | SI | Lipidos  C |
| Q44 | - |  |  | SI | Lipidos  VG |
| Q45 | - |  |  | SI | Lipidos  VLC |
| Q46 | - |  |  | SI | Lipidos  F |
| Q47 | - |  |  | SI | Lipidos  CAG	 |
| Q48 | - |  |  | SI | Lipidos  CBG	 |
| Q49 | - |  |  | SI | Lipidos  LG |
| Q50 | - |  |  | SI | Lipidos  LAG	 |
| Q51 | - |  |  | SI | Lipidos  LMG	 |
| Q52 | - |  |  | SI | Lipidos  LBG	 |
| Q53 | - |  |  | SI | Lipidos  Q |
| Q54 | - |  |  | SI | Lipidos  AyG	 |
| Q55 | - |  |  | SI | Lipidos  ARL	 |
| Q56 | - |  |  | SI | Lipidos  AZ |
| Q57 | - |  |  | SI | Proteínas  C |
| Q58 | - |  |  | SI | Proteínas  VG |
| Q59 | - |  |  | SI | proteínas  VLC |
| Q60 | - |  |  | SI | proteínas  F	 |
| Q61 | - |  |  | SI | proteínas  CAG |
| Q62 | - |  |  | SI | proteínas  CBG |
| Q63 | - |  |  | SI | proteínas  LG |
| Q64 | - |  |  | SI | proteínas  LAG |
| Q65 | - |  |  | SI | proteínas  LMG |
| Q66 | - |  |  | SI | proteínas  LBG |
| Q67 | - |  |  | SI | proteínas  Q	 |
| Q68 | - |  |  | SI | proteínas  AyG |
| Q69 | - |  |  | SI | proteínas  ARL |
| Q70 | - |  |  | SI | proteínas  AZ |
| Q71 | - |  |  | SI | Total Calorias |
| Q72 | - |  |  | SI | Total CHO |
| Q73 | - |  |  | SI | Total Lipidos |
| Q74 | - |  |  | SI | Total Proteinas |
| Q75 | - |  |  | SI | Total Porciones |
| Q76 | - |  |  | SI | Recomendado C |
| Q77 | - |  |  | SI | Recomendado CHO |
| Q78 | - |  |  | SI | Recomendado L |
| Q79 | - |  |  | SI | Recomendado P |
| Q80 | - |  |  | SI | Adecuacion C |
| Q81 | - |  |  | SI | Adecuacion CHO |
| Q82 | - |  |  | SI | Adecuacion L |
| Q83 | - |  |  | SI | Adecuacion P |
| Q84 | - |  |  | SI | P % |
| Q86 | - |  |  | SI | CHO % |
| Q87 | - |  |  | SI | Peso Transversal |
| Q87ObsDR | - |  |  | SI | Peso Transversal DR |
| Q88 | - |  |  | SI | G % |
| Q89 | - |  |  | SI | TOTAL CALORIAS |
| Q90 | - |  |  | SI | TOTAL PROTEINAS |
| Q91 | - |  |  | SI | TOTAL CHO |
| Q92 | - |  |  | SI | TOTAL LIPIDOS |
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