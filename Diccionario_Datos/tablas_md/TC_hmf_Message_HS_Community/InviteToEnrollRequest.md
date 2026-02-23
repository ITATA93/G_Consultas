# TC_hmf_Message_HS_Community.InviteToEnrollRequest

**Schema:** TC_hmf_Message_HS_Community
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Inventario**. Gestión de stock y bodega.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ContentKey | varchar |  |  | SI | Link to a custom message that the patient will rec... |
| Email | varchar |  |  | SI | Email Address.  Patient will receive an email invi... |
| LanguageCode | varchar |  |  | SI | Language Code.  Typically an ISO Code (e.g. "en", ... |
| MRN | varchar |  |  | SI | Medical Record Number. |
| MobilePhone | varchar |  |  | SI | Mobile Phone Number. |
| Name | varchar |  |  | NO | Patient Name.  Typically formatted "FirstName Surn... |
| PhoneProvider | varchar |  |  | SI | Phone Provider.  (e.g. "Verizon", "AT&T Wireless")... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*