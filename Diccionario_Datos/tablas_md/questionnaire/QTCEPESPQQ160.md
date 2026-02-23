# questionnaire.QTCEPESPQQ160

> Doc. Intra-Operatoria Proc. Específicos : Dispositivos

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Doc. Intra-Operatoria Proc. Específicos : Dispositivos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q160Q1 | varchar |  |  | SI | Acción |
| Q160Q2 | varchar |  |  | SI | Tipo de Dispositivo |
| Q160Q3 | varchar |  |  | SI | Medida |
| Q160Q4 | varchar |  |  | SI | Ubicación |
| Q160Q5 | numeric |  |  | SI | Número de Intentos de Instalación |
| Q160Q6 | varchar |  |  | SI | Médico Responsable Indicación |
| Q160Q7 | varchar |  |  | SI | Responsable Instalación/Retiro |
| Q160Q8 | date |  |  | SI | Fecha |
| Q160Q9 | time |  |  | SI | Hora |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*