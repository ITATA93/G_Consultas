# SQLUser.SS_HL7MasterFile

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7MFD_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7MFD_Count | double |  |  | NO | Count - Always 1 |
| HL7MFD_M05BedActive | varchar |  |  | SI | M05 Mark Bed as Active |
| HL7MFD_M05BedAvail | varchar |  |  | SI | M05 Mark Bed as Available |
| HL7MFD_M05DefBedType | varchar |  |  | SI | M05 Default Bed Type |
| HL7MFD_M05DefRoomType | varchar |  |  | SI | M05 Default Room Type |
| HL7MFD_M05DefWardType | varchar |  |  | SI | M05 Default Ward Type |
| HL7MFD_M05WardAsInpat | varchar |  |  | SI | M05 Mark Ward as Inpatient |
| HL7MFD_M08DefAccessProf | varchar |  |  | SI | M08 Default Access Profile |
| HL7MFD_M08DefBillingSubGrp | varchar |  |  | SI | M08 Default Billing Sub Group |
| HL7MFD_M08DefSecurityGrp | varchar |  |  | SI | M08 Default Security Group |
| HL7MFD_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*