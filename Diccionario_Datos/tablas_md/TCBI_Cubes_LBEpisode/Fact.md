# TCBI_Cubes_LBEpisode.Fact

**Schema:** TCBI_Cubes_LBEpisode
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1098546747 | varchar |  |  | SI | Dimension: Dx1098546747<br/>
Source: LBEPReceived... |
| Dx1654921406 | varchar |  |  | SI | Dimension: Dx1654921406<br/>
Source: LBEPHoldRemo... |
| Dx1671668779 | varchar |  |  | SI | Dimension: Dx1671668779<br/>
Source: LBEPEntryDat... |
| Dx1917683474 | varchar |  |  | SI | Dimension: Dx1917683474<br/>
Source: LBEPHoldSetD... |
| Dx2015746969 | bigint |  |  | SI | Dimension: Dx2015746969
Expression: %source.LBEPH... |
| Dx2404009592 | varchar |  |  | SI | Dimension: Dx2404009592<br/>
Source: LBEPEntryDat... |
| Dx2613327538 | varchar |  |  | SI | Dimension: Dx2613327538<br/>
Source: LBEPHoldSetD... |
| Dx2968690538 | varchar |  |  | SI | Dimension: Dx2968690538<br/>
Source: LBEPHoldRemo... |
| Dx3082992757 | varchar |  |  | SI | Dimension: Dx3082992757<br/>
Source: LBEPEntryDat... |
| Dx3119666751 | bigint |  |  | SI | Dimension: Dx3119666751
Expression: %source.LBEPH... |
| Dx3370650260 | varchar |  |  | SI | Dimension: Dx3370650260<br/>
Source: LBEPEntryDat... |
| Dx3439250918 | bigint |  |  | SI | Dimension: Dx3439250918
Expression: $ztime(%sourc... |
| Dx3456968118 | varchar |  |  | SI | Dimension: Dx3456968118<br/>
Source: LBEPHoldRemo... |
| Dx3472792696 | varchar |  |  | SI | Dimension: Dx3472792696<br/>
Source: LBEPCollecti... |
| Dx3519333899 | varchar |  |  | SI | Dimension: Dx3519333899<br/>
Source: LBEPCollecti... |
| Dx3604145667 | varchar |  |  | SI | Dimension: Dx3604145667<br/>
Source: LBEPHoldSetD... |
| Dx3704650557 | varchar |  |  | SI | Dimension: Dx3704650557<br/>
Source: LBEPHoldRemo... |
| Dx4001009371 | bigint |  |  | SI | Dimension: Dx4001009371
Expression: $ztime(%sourc... |
| Dx4080291134 | varchar |  |  | SI | Dimension: Dx4080291134<br/>
Source: LBEPCollecti... |
| Dx4093910121 | bigint |  |  | SI | Dimension: Dx4093910121
Expression: %source.LBEPE... |
| Dx4259894060 | varchar |  |  | SI | Dimension: Dx4259894060<br/>
Source: LBEPHoldSetD... |
| Dx587000754 | varchar |  |  | SI | Dimension: Dx587000754<br/>
Source: LBEPReceivedD... |
| Dx680333575 | bigint |  |  | SI | Dimension: Dx680333575
Expression: $ztime(%source... |
| Dx739853228 | varchar |  |  | SI | Dimension: Dx739853228<br/>
Source: LBEPReceivedD... |
| Dx809081198 | varchar |  |  | SI | Dimension: Dx809081198<br/>
Source: LBEPHoldRemov... |
| Dx976946256 | varchar |  |  | SI | Dimension: Dx976946256<br/>
Source: LBEPHoldSetDa... |
| DxAccountClass | bigint |  |  | SI | Dimension: DxAccountClass<br/>
Source: LBEPAccoun... |
| DxAgeRange | bigint |  |  | SI | Dimension: DxAgeRange
Expression: %source.LBEPAge |
| DxCareProviderGroup | bigint |  |  | SI | Dimension: DxCareProviderGroup<br/>
Source: LBEPC... |
| DxCareProviderName | bigint |  |  | SI | Dimension: DxCareProviderName<br/>
Source: LBEPCa... |
| DxCity | bigint |  |  | SI | Dimension: DxCity
Expression: %expression.GetLabE... |
| DxCloseDayOfWeek | bigint |  |  | SI | Dimension: DxCloseDayOfWeek
Expression: ##class(T... |
| DxCoastCenter | bigint |  |  | SI | Dimension: DxCoastCenter<br/>
Source: LBEPPatient... |
| DxCountry | bigint |  |  | SI | Dimension: DxCountry
Expression: %expression.GetL... |
| DxCounty | bigint |  |  | SI | Dimension: DxCounty
Expression: %expression.GetLa... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: %ID |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBEPPAPers... |
| DxDepartment | bigint |  |  | SI | Dimension: DxDepartment<br/>
Source: LBEPPatientL... |
| DxEntryDayOfWeek | bigint |  |  | SI | Dimension: DxEntryDayOfWeek
Expression: ##class(T... |
| DxExternalReferralNumber | bigint |  |  | SI | Dimension: DxExternalReferralNumber<br/>
Source: ... |
| DxExternalReferralSource | bigint |  |  | SI | Dimension: DxExternalReferralSource<br/>
Source: ... |
| DxFacility | bigint |  |  | SI | Dimension: DxFacility<br/>
Source: LBEPFacilityDR... |
| DxFacilityType | bigint |  |  | SI | Dimension: DxFacilityType<br/>
Source: LBEPFacili... |
| DxHoldRemovalSecurityGroup | bigint |  |  | SI | Dimension: DxHoldRemovalSecurityGroup<br/>
Source... |
| DxHoldRemovalUserName | bigint |  |  | SI | Dimension: DxHoldRemovalUserName<br/>
Source: LBE... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: LBEPPatientLoc... |
| DxLBEPAge | bigint |  |  | SI | Dimension: DxLBEPAge<br/>
Source: LBEPAge |
| DxLBEPClinicalConditions | varchar |  |  | SI | Dimension: DxLBEPClinicalConditions
Expression: %... |
| DxLBEPClinicalDetails | varchar |  |  | SI | Dimension: DxLBEPClinicalDetails
Expression: %exp... |
| DxLBEPCollectionDate | integer |  |  | SI | Dimension: DxLBEPCollectionDate<br/>
Source: LBEP... |
| DxLBEPCollectionDateFxDays | varchar |  |  | SI | Dimension: DxLBEPCollectionDateFxDays<br/>
Source... |
| DxLBEPCollectionDateFxYear | varchar |  |  | SI | Dimension: DxLBEPCollectionDateFxYear<br/>
Source... |
| DxLBEPDOB | date |  |  | SI | Dimension: DxLBEPDOB<br/>
Source: LBEPDOB |
| DxLBEPDOBFxDayMonthYear | varchar |  |  | SI | Dimension: DxLBEPDOBFxDayMonthYear<br/>
Source: L... |
| DxLBEPDOBFxMonthYear | varchar |  |  | SI | Dimension: DxLBEPDOBFxMonthYear<br/>
Source: LBEP... |
| DxLBEPDOBFxYear | varchar |  |  | SI | Dimension: DxLBEPDOBFxYear<br/>
Source: LBEPDOB |
| DxLBEPEntryDate | date |  |  | SI | Dimension: DxLBEPEntryDate<br/>
Source: LBEPEntry... |
| DxLBEPEntryDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBEPEntryDateFxMonthYear<br/>
Source... |
| DxLBEPEntryDateFxYear | varchar |  |  | SI | Dimension: DxLBEPEntryDateFxYear<br/>
Source: LBE... |
| DxLBEPHoldRemoveDate | date |  |  | SI | Dimension: DxLBEPHoldRemoveDate<br/>
Source: LBEP... |
| DxLBEPHoldRemoveDateFxYear | varchar |  |  | SI | Dimension: DxLBEPHoldRemoveDateFxYear<br/>
Source... |
| DxLBEPHoldSetDate | date |  |  | SI | Dimension: DxLBEPHoldSetDate<br/>
Source: LBEPHol... |
| DxLBEPHoldSetDateFxYear | varchar |  |  | SI | Dimension: DxLBEPHoldSetDateFxYear<br/>
Source: L... |
| DxLBEPReceivedDate | date |  |  | SI | Dimension: DxLBEPReceivedDate<br/>
Source: LBEPRe... |
| DxLBEPReceivedDateFxYear | varchar |  |  | SI | Dimension: DxLBEPReceivedDateFxYear<br/>
Source: ... |
| DxLBEPReferringDoctor | bigint |  |  | SI | Dimension: DxLBEPReferringDoctor
Expression: %exp... |
| DxLBEPSecondaryReferringDoctor | bigint |  |  | SI | Dimension: DxLBEPSecondaryReferringDoctor
Express... |
| DxLabSite | bigint |  |  | SI | Dimension: DxLabSite<br/>
Source: LBEPLabSiteDR.C... |
| DxLocationType | bigint |  |  | SI | Dimension: DxLocationType<br/>
Source: LBEPPatien... |
| DxOnHoldSecurityGroup | bigint |  |  | SI | Dimension: DxOnHoldSecurityGroup<br/>
Source: LBE... |
| DxOnHoldUserName | bigint |  |  | SI | Dimension: DxOnHoldUserName<br/>
Source: LBEPHold... |
| DxOpenDayOfWeek | bigint |  |  | SI | Dimension: DxOpenDayOfWeek
Expression: ##class(TC... |
| DxPatientLocation | bigint |  |  | SI | Dimension: DxPatientLocation<br/>
Source: LBEPPat... |
| DxPatientType | bigint |  |  | SI | Dimension: DxPatientType<br/>
Source: LBEPPatType... |
| DxPostCode | bigint |  |  | SI | Dimension: DxPostCode
Expression: %expression.Get... |
| DxPregnant | bigint |  |  | SI | Dimension: DxPregnant<br/>
Source: LBEPPregnant |
| DxPriority | bigint |  |  | SI | Dimension: DxPriority<br/>
Source: LBEPPriorityDR... |
| DxREFDType | bigint |  |  | SI | Dimension: DxREFDType<br/>
Source: LBEPReferringD... |
| DxReceivingDayOfWeek | bigint |  |  | SI | Dimension: DxReceivingDayOfWeek
Expression: ##cla... |
| DxReceivingTime | bigint |  |  | SI | Dimension: DxReceivingTime
Expression: $ztime(%so... |
| DxReceivingTimeRange | bigint |  |  | SI | Dimension: DxReceivingTimeRange
Expression: %sour... |
| DxReqDoctor | bigint |  |  | SI | Dimension: DxReqDoctor
Expression: %expression.Ge... |
| DxReqType | bigint |  |  | SI | Dimension: DxReqType
Expression: %expression.ReqT... |
| DxRequestingLocation | bigint |  |  | SI | Dimension: DxRequestingLocation<br/>
Source: LBEP... |
| DxSecondaryREFDType | bigint |  |  | SI | Dimension: DxSecondaryREFDType<br/>
Source: LBEPS... |
| DxSecurityGroup | bigint |  |  | SI | Dimension: DxSecurityGroup<br/>
Source: LBEPUserD... |
| DxSex | bigint |  |  | SI | Dimension: DxSex<br/>
Source: LBEPSexDR.CTSEXDesc |
| DxSpeciality | bigint |  |  | SI | Dimension: DxSpeciality<br/>
Source: LBEPCareProv... |
| DxSpecies | bigint |  |  | SI | Dimension: DxSpecies<br/>
Source: LBEPSpeciesDR.L... |
| DxSpeciesBreed | bigint |  |  | SI | Dimension: DxSpeciesBreed<br/>
Source: LBEPSpecie... |
| DxState | bigint |  |  | SI | Dimension: DxState
Expression: %expression.GetLab... |
| DxSubSpeciality | bigint |  |  | SI | Dimension: DxSubSpeciality<br/>
Source: LBEPCareP... |
| DxSubjectType | bigint |  |  | SI | Dimension: DxSubjectType
Expression: %expression.... |
| DxUserName | bigint |  |  | SI | Dimension: DxUserName<br/>
Source: LBEPUserDR.SSU... |
| RxIDViaLBEPPAAdmDR | bigint |  | FK | SI | Relationship: RxIDViaLBEPPAAdmDR<br/>
Source: LBE... |
| RxIDViaLBEPSubjectDR | bigint |  | FK | SI | Relationship: RxIDViaLBEPSubjectDR<br/>
Source: L... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*