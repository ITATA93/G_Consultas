# TCDS_Cubes_LBEpisode.Fact

**Schema:** TCDS_Cubes_LBEpisode
**Columnas:** 64
**Actualizado:** 2026-01-30 15:30:29

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1098546747 | varchar |  |  | SI | Dimension: Dx1098546747<br/>
Source: LBEPReceived... |
| Dx3472792696 | varchar |  |  | SI | Dimension: Dx3472792696<br/>
Source: LBEPCollecti... |
| Dx3519333899 | varchar |  |  | SI | Dimension: Dx3519333899<br/>
Source: LBEPCollecti... |
| Dx4080291134 | varchar |  |  | SI | Dimension: Dx4080291134<br/>
Source: LBEPCollecti... |
| Dx587000754 | varchar |  |  | SI | Dimension: Dx587000754<br/>
Source: LBEPReceivedD... |
| Dx739853228 | varchar |  |  | SI | Dimension: Dx739853228<br/>
Source: LBEPReceivedD... |
| DxAgeRange | bigint |  |  | SI | Dimension: DxAgeRange
Expression: %source.LBEPAge |
| DxCareProviderGroup | bigint |  |  | SI | Dimension: DxCareProviderGroup<br/>
Source: LBEPC... |
| DxCareProviderName | bigint |  |  | SI | Dimension: DxCareProviderName<br/>
Source: LBEPCa... |
| DxCity | bigint |  |  | SI | Dimension: DxCity
Expression: %expression.GetLabE... |
| DxCoastCenter | bigint |  |  | SI | Dimension: DxCoastCenter<br/>
Source: LBEPPatient... |
| DxCollectionTime | bigint |  |  | SI | Dimension: DxCollectionTime<br/>
Source: LBEPColl... |
| DxCountry | bigint |  |  | SI | Dimension: DxCountry
Expression: %expression.GetL... |
| DxCounty | bigint |  |  | SI | Dimension: DxCounty
Expression: %expression.GetLa... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: %ID |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBEPSubj... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBEPPAPers... |
| DxDepartment | bigint |  |  | SI | Dimension: DxDepartment<br/>
Source: LBEPPatientL... |
| DxDoctorID | bigint |  |  | SI | Dimension: DxDoctorID<br/>
Source: LBEPCareProvDR... |
| DxFacility | bigint |  |  | SI | Dimension: DxFacility<br/>
Source: LBEPFacilityDR... |
| DxFacilityType | bigint |  |  | SI | Dimension: DxFacilityType<br/>
Source: LBEPFacili... |
| DxFasting | bigint |  |  | SI | Dimension: DxFasting
Expression: %expression.Fast... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: LBEPPatientLoc... |
| DxLBEPAccountClasses | bigint |  |  | SI | Dimension: DxLBEPAccountClasses<br/>
Source: LBEP... |
| DxLBEPAge | bigint |  |  | SI | Dimension: DxLBEPAge<br/>
Source: LBEPAge |
| DxLBEPClinicalConditions | varchar |  |  | SI | Dimension: DxLBEPClinicalConditions
Expression: %... |
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
| DxLBEPExternalReferralSources | bigint |  |  | SI | Dimension: DxLBEPExternalReferralSources<br/>
Sou... |
| DxLBEPPregnantNumberOfWeeks | bigint |  |  | SI | Dimension: DxLBEPPregnantNumberOfWeeks<br/>
Sourc... |
| DxLBEPReceivedDate | date |  |  | SI | Dimension: DxLBEPReceivedDate<br/>
Source: LBEPRe... |
| DxLBEPReceivedDateFxYear | varchar |  |  | SI | Dimension: DxLBEPReceivedDateFxYear<br/>
Source: ... |
| DxLBEPReferringDoctors | bigint |  |  | SI | Dimension: DxLBEPReferringDoctors
Expression: %ex... |
| DxLBEPSecondaryReferringDoctorss | bigint |  |  | SI | Dimension: DxLBEPSecondaryReferringDoctorss
Expre... |
| DxLabSite | bigint |  |  | SI | Dimension: DxLabSite<br/>
Source: LBEPLabSiteDR.C... |
| DxLocationType | bigint |  |  | SI | Dimension: DxLocationType<br/>
Source: LBEPPatien... |
| DxOnHold | bigint |  |  | SI | Dimension: DxOnHold
Expression: %expression.OnHol... |
| DxPatientLocation | bigint |  |  | SI | Dimension: DxPatientLocation<br/>
Source: LBEPPat... |
| DxPatientType | bigint |  |  | SI | Dimension: DxPatientType<br/>
Source: LBEPPatType... |
| DxPostCode | bigint |  |  | SI | Dimension: DxPostCode
Expression: %expression.Get... |
| DxPregnant | bigint |  |  | SI | Dimension: DxPregnant
Expression: %expression.Pat... |
| DxPriority | bigint |  |  | SI | Dimension: DxPriority<br/>
Source: LBEPPriorityDR... |
| DxREFDType | bigint |  |  | SI | Dimension: DxREFDType<br/>
Source: LBEPReferringD... |
| DxReceivedTime | bigint |  |  | SI | Dimension: DxReceivedTime<br/>
Source: LBEPReceiv... |
| DxReceivingDayOfWeek | bigint |  |  | SI | Dimension: DxReceivingDayOfWeek
Expression: ##cla... |
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
| DxSubjectType | bigint |  |  | SI | Dimension: DxSubjectType<br/>
Source: LBEPSubject... |
| DxUserName | bigint |  |  | SI | Dimension: DxUserName<br/>
Source: LBEPUserDR.SSU... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*