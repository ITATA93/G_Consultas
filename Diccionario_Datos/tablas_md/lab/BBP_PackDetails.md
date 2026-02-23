# lab.BBP_PackDetails

**Schema:** lab
**Columnas:** 48
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBP_RowID | varchar | PK |  | NO | - |
| BBP_128_DivisionLevel | varchar |  |  | SI | 128 Division Level |
| BBP_128_DonationType | varchar |  |  | SI | 128 Donation Type |
| BBP_128_IntendedUse | varchar |  |  | SI | 128 Intended Use |
| BBP_128_ManufCatNo | varchar |  |  | SI | 128 Manuf CatNo |
| BBP_128_ManufID_DR | varchar |  | FK | SI | 128 ManufID DR |
| BBP_128_ManufLotNo | varchar |  |  | SI | 128 Manuf LotNo |
| BBP_128_SpecialTesting | varchar |  |  | SI | 128 Special Testing |
| BBP_Autologous | varchar |  |  | SI | Autologous |
| BBP_BloodGroupEntered_DR | varchar |  | FK | SI | Blood Group Entered DR |
| BBP_BloodGroup_DR | varchar |  | FK | SI | Blood Group DR |
| BBP_BloodProduct_DR | varchar |  | FK | SI | Blood Product DR |
| BBP_DateExpired | date |  |  | SI | Date Expired |
| BBP_DateOfCollection | date |  |  | SI | Date Of Collection |
| BBP_DateOfProduction | date |  |  | SI | Date Of Production |
| BBP_DateReceived | date |  |  | SI | Date Received |
| BBP_DeliveryNumber | varchar |  |  | SI | Delivery Number |
| BBP_DonorDebtor_DR | varchar |  | FK | SI | Donor Debtor |
| BBP_Donor_ID | varchar |  |  | SI | Donor ID |
| BBP_LabelPrinted_Date | date |  |  | SI | Label Printed Date |
| BBP_LabelPrinted_MRN_DR | varchar |  | FK | SI | Label Printed MRN DR |
| BBP_LockedFields | varchar |  |  | SI | Locked Fields |
| BBP_PackID | varchar |  |  | NO | Pack ID |
| BBP_PackVolume | varchar |  |  | SI | Pack Volume |
| BBP_ParentPack_DR | varchar |  | FK | SI | Parent Pack DR |
| BBP_ReceivedByDonorModule | varchar |  |  | SI | Received By Donor Module |
| BBP_Remarks | varchar |  |  | SI | Remarks |
| BBP_SecondIdentifier | varchar |  |  | NO | Second Identifier |
| BBP_Supplier_DR | varchar |  | FK | SI | Supplier DR |
| BBP_TimeExpired | time |  |  | SI | Time Expired |
| BBP_TimeOfCollection | time |  |  | SI | Time Of Collection |
| BBP_TimeOfProduction | time |  |  | SI | Time Of Production |
| BBP_TimeReceived | time |  |  | SI | Time Received |
| BBP_UserReceived_DR | varchar |  | FK | SI | User Received DR |
| BBP_Value | double |  |  | SI | Pack Value |
| BBP_do_Location_DR | varchar |  | FK | SI | Location DR |
| BBP_do_PatientDebtor_DR | varchar |  | FK | SI | Patient Debtor DR |
| BBP_do_ProductGroup_DR | varchar |  | FK | SI | Product Group DR |
| BBP_do_StatusReserve | varchar |  |  | SI | Status Reserve |
| BBP_do_StatusStock | varchar |  |  | SI | Status Stock |
| BBP_do_Status_DR | varchar |  | FK | SI | Status of Pack DR |
| BBP_do_VisitTS_DR | varchar |  | FK | SI | Visit TS DR |
| BBP_xxx2 | varchar |  |  | SI | 128 Anti c |
| BBP_xxx3 | varchar |  |  | SI | 128 Anti C |
| BBP_xxx4 | varchar |  |  | SI | 128 Anti e |
| BBP_xxx5 | varchar |  |  | SI | 128 Anti E |
| BBP_xxx6 | varchar |  |  | SI | 128 Mi III |
| BBP_xxx7 | varchar |  |  | SI | Genotype DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*